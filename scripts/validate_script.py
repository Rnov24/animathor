#!/usr/bin/env python3
"""
Animathor Script & Code Quality Validator (Anti-Slop & Accuracy Linter v2.0)
Audits storyboards (markdown) and animation scripts (python) against:
- Rule R-02: Zero Em Dashes (Unicode U+2014)
- Anti-Slop: Banned English AI clichés and marketing buzzwords
- Pre-Flight Math Gate: Mandatory verification section in storyboards
- Dynamic Pacing Budget: Words-per-second speech constraints (<= 2.3 wps) in AV tables
- Visual Breathing Room: Mandatory pauses (self.wait >= 1.5s) after key reveals
- Safe Zone Buffers: Platform overlay clearance for vertical 9:16 scripts
- Technical Integrity: LaTeX raw strings, Monospace font guard, clean scene exits
- Inline Suppression: Support for # animathor: ignore or <!-- animathor: ignore -->
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows console
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BANNED_AI_WORDS = [
    r"\bdelve\b",
    r"\bdelving\b",
    r"\bunlock(?:ing|s|ed)?\b",
    r"\brevolution(?:ary|ize|izing|ized)?\b",
    r"\bgame[ -]changer\b",
    r"\btapestry\b",
    r"\bmind[ -]blowing\b",
    r"\bseamless(?:ly)?\b",
    r"\bat its core\b",
    r"\bfundamentally\b",
    r"\bwithout further ado\b",
    r"\bhave you ever wondered\b",
    r"\bimagine a world\b",
    r"\btestament to\b",
    r"\brobust\b",
    r"\bcutting[ -]edge\b",
    r"\belevate\b",
    r"\bempower\b",
    r"\bparamount\b",
    r"\bcrucial role\b",
    r"\bbeacon of\b",
    r"\bsupercharge\b",
    r"\bunleash\b",
    r"\bin conclusion\b",
    r"\bto summarize\b",
    r"\brich tapestry\b",
    r"\bfoster(?:ing)?\b",
    r"\bplethora\b",
    r"\bmyriad\b",
    r"\bmeticulous(?:ly)?\b",
    r"\bintricate dance\b",
    r"\bsymphony of\b",
]

SUPPRESSION_PATTERNS = [
    re.compile(r"#\s*animathor:\s*ignore", re.IGNORECASE),
    re.compile(r"<!--\s*animathor:\s*ignore\s*-->", re.IGNORECASE),
    re.compile(r"#\s*noqa", re.IGNORECASE),
    re.compile(r"<!--\s*noqa\s*-->", re.IGNORECASE),
]


def is_suppressed(line: str) -> bool:
    """Check if line contains an inline suppression comment."""
    return any(pat.search(line) for pat in SUPPRESSION_PATTERNS)


class ScriptValidator:
    def __init__(self, filepath: str | Path, json_mode: bool = False):
        self.path = Path(filepath)
        self.json_mode = json_mode
        self.findings: list[tuple[str, int, str]] = []  # (severity, line_num, message)

    def audit(self) -> bool:
        if not self.path.exists():
            if self.json_mode:
                print(json.dumps({"error": f"File '{self.path}' does not exist.", "status": "ERROR"}))
            else:
                print(f"[!] Error: File '{self.path}' does not exist.")
            return False

        content = self.path.read_text(encoding="utf-8", errors="replace")
        lines = content.splitlines()

        if self.path.suffix.lower() == ".md":
            self._audit_markdown(lines, content)
        elif self.path.suffix.lower() == ".py":
            self._audit_python(lines, content)
        else:
            self._audit_markdown(lines, content)

        self._print_report()
        has_critical = any(sev == "FAIL" for sev, _, _ in self.findings)
        return not has_critical

    def _audit_markdown(self, lines: list[str], content: str):
        # 1. Em Dash & En Dash Check (Rule R-02)
        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            if "\u2014" in line:
                self.findings.append(("FAIL", i, "Rule R-02: Em dash character (U+2014) detected. Use a comma, colon, or period."))
            if " – " in line:
                self.findings.append(("WARN", i, "En dash (' – ') used as parenthetical separator. Replace with comma or colon."))

        # 2. Banned English AI Buzzwords
        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            for pattern in BANNED_AI_WORDS:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    word = match.group(0)
                    self.findings.append(("FAIL", i, f"Anti-Slop: Banned AI cliché '{word}' detected. State the concept directly."))

        # 3. Exclamation Stuffing Check
        exclamations = sum(1 for line in lines if not is_suppressed(line) for ch in line if ch == "!")
        if exclamations > 3:
            self.findings.append(("WARN", 0, f"Exclamation count ({exclamations}) is high. Aim for <= 2 in technical cinema."))

        # 4. Mandatory Mathematical Pre-Flight Audit Gate
        is_storyboard = "storyboard" in self.path.name.lower() or any("|" in line for line in lines[:30])
        if is_storyboard:
            has_preflight = re.search(
                r"#+\s*(?:\d+\.\s*)?.*(?:Mathematical|Math|Pre-Flight).*Audit",
                content,
                re.IGNORECASE
            )
            if not has_preflight:
                self.findings.append((
                    "FAIL", 0,
                    "Pre-Flight Audit: Missing mandatory 'Mathematical Pre-Flight Audit' section in storyboard."
                ))

        # 5. Dynamic AV Table Pacing & Word Budget Scanner
        self._audit_av_table(lines)

    def _audit_av_table(self, lines: list[str]):
        """Parses Markdown AV tables dynamically regardless of column order or count."""
        table_lines: list[tuple[int, str]] = []
        in_table = False

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                if not in_table:
                    in_table = True
                table_lines.append((i, stripped))
            else:
                if in_table:
                    self._process_table_block(table_lines)
                    table_lines = []
                    in_table = False

        if table_lines:
            self._process_table_block(table_lines)

    def _process_table_block(self, table_lines: list[tuple[int, str]]):
        if len(table_lines) < 3:
            return  # Need header, delimiter, and at least one data row

        # Extract header columns
        _, header_raw = table_lines[0]
        header_cols = [c.strip().lower() for c in header_raw.strip("|").split("|")]

        beat_idx = -1
        narration_idx = -1

        for idx, col in enumerate(header_cols):
            if any(k in col for k in ["beat", "durasi", "duration", "time", "waktu"]):
                if beat_idx == -1:
                    beat_idx = idx
            if any(k in col for k in ["narasi", "narration", "voiceover", "spoken", "speech", "audio", "naskah"]):
                if narration_idx == -1:
                    narration_idx = idx

        # Fallback column heuristics if headers differ
        if beat_idx == -1:
            beat_idx = 0
        if narration_idx == -1 and len(header_cols) >= 4:
            narration_idx = 3

        # Process data rows (skip header and delimiter at index 0 and 1)
        for line_num, row_raw in table_lines[2:]:
            cols = [c.strip() for c in row_raw.strip("|").split("|")]
            if len(cols) <= max(beat_idx, narration_idx):
                continue

            beat_cell = cols[beat_idx]
            narration_cell = cols[narration_idx]

            # 1. Extract duration
            duration = self._extract_duration(beat_cell)
            if not duration or duration <= 0:
                continue

            # 2. Extract spoken text
            words_count = self._extract_spoken_word_count(narration_cell)
            if words_count == 0:
                continue

            wps = words_count / duration
            if wps > 2.3:
                self.findings.append((
                    "FAIL", line_num,
                    f"Pacing Overload: Beat ({duration:.1f}s) has {words_count} words ({wps:.2f} words/sec). Max allowed is 2.3 wps."
                ))

    def _extract_duration(self, text: str) -> float | None:
        """Extracts seconds from timecodes or duration labels."""
        # Matches: *(10 detik)*, 10s, 10 seconds, 10.5s
        sec_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:detik|seconds|sec|s\b)", text, re.IGNORECASE)
        if sec_match:
            return float(sec_match.group(1))

        # Matches range: 00:00 - 00:10
        tc_match = re.search(r"(\d{2}):(\d{2})\s*-\s*(\d{2}):(\d{2})", text)
        if tc_match:
            m1, s1, m2, s2 = map(int, tc_match.groups())
            start = m1 * 60 + s1
            end = m2 * 60 + s2
            if end > start:
                return float(end - start)
        return None

    def _extract_spoken_word_count(self, text: str) -> int:
        """Extracts spoken word count, supporting quoted speech or cleaned prose."""
        # Check quoted speech first: "..." or '...' or “...” or «...»
        quote_match = re.search(r'["\'“«]([^"\'”»]{3,})["\'”»]', text, re.DOTALL)
        if quote_match:
            spoken_text = quote_match.group(1)
            # Remove punctuation and count
            words = [w for w in re.split(r"\s+", spoken_text.strip()) if w]
            return len(words)

        # Fallback: strip markdown formatting annotations like *(10 kata • 1.0 wps)*
        cleaned = re.sub(r"\*\(.*?\)\*", "", text)
        cleaned = re.sub(r"\*\*.*?\*\*:", "", cleaned)
        cleaned = re.sub(r"<[^>]+>", " ", cleaned)
        words = [w for w in re.split(r"\s+", cleaned.strip()) if len(w) > 1 and not w.startswith("|")]
        return len(words)

    def _audit_python(self, lines: list[str], content: str):
        # 1. Em Dash in Strings or Comments
        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            if "\u2014" in line:
                self.findings.append(("FAIL", i, "Rule R-02: Em dash character (U+2014) in Python string or comment."))

        # 2. Monospace Font Guard
        has_mono = re.search(r'MONO\s*=\s*["\'](Consolas|Menlo|DejaVu Sans Mono|Courier)', content)
        if not has_mono and "Scene" in content:
            self.findings.append(("FAIL", 0, "Pango Kerning Guard: No MONO font defined (must use Consolas, Menlo, or DejaVu Sans Mono)."))

        # 3. LaTeX Raw String Escaping Guard
        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            # Matches MathTex("...") or Tex("...") where backslash is not preceded by r or R
            bad_mathtex = re.search(r'(?<![rR])MathTex\(\s*["\']\\[a-zA-Z]', line)
            bad_tex = re.search(r'(?<![rR])Tex\(\s*["\']\\[a-zA-Z]', line)
            if bad_mathtex or bad_tex:
                self.findings.append(("FAIL", i, "LaTeX Syntax: MathTex/Tex string missing raw prefix r'...' or R'...'. Python will escape backslashes."))

        # 4. Banned Buzzwords in Python code
        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            for pattern in BANNED_AI_WORDS:
                if re.search(pattern, line, re.IGNORECASE):
                    self.findings.append(("WARN", i, f"Anti-Slop: Potential AI buzzword in line: {line.strip()[:65]}"))

        # 5. Visual Breathing Room Guard (self.wait >= 1.5s after major reveals)
        self._audit_breathing_room(content)

        # 6. Safe Zone Buffers for 9:16 Vertical Video
        self._audit_vertical_safe_zones(lines, content)

        # 7. Clean Scene Exit Guard
        self._audit_scene_exits(content)

    def _audit_breathing_room(self, content: str):
        """Verifies that scene animations include necessary viewer breathing pauses."""
        # Find scene classes
        scene_blocks = re.findall(r"class\s+([A-Za-z0-9_]+)\s*\([^)]*Scene[^)]*\):([\s\S]*?)(?=\nclass|\Z)", content)
        for scene_name, block in scene_blocks:
            play_count = len(re.findall(r"\bself\.play\(", block))
            wait_matches = re.findall(r"\bself\.wait\(\s*([0-9.]+)?\s*\)", block)

            if play_count >= 3 and len(wait_matches) == 0:
                self.findings.append((
                    "FAIL", 0,
                    f"Breathing Room: Scene '{scene_name}' contains {play_count} animations but zero self.wait() calls. Add 1.5s to 2.5s pauses after major reveals."
                ))
            elif play_count >= 3 and len(wait_matches) > 0:
                # Check durations of waits
                durations = [float(w) if w else 1.0 for w in wait_matches]
                max_wait = max(durations)
                if max_wait < 1.0:
                    self.findings.append((
                        "WARN", 0,
                        f"Breathing Room: Scene '{scene_name}' only has micro-pauses (max: {max_wait}s). Major visual reveals require self.wait(1.5) to self.wait(2.5)."
                    ))

    def _audit_vertical_safe_zones(self, lines: list[str], content: str):
        """Checks for unsafe edge placements in 9:16 vertical shorts."""
        is_vertical = (
            "1080x1920" in content.replace(" ", "") or
            "9:16" in content or
            bool(re.search(r"pixel_height\s*=\s*1920", content)) or
            bool(re.search(r"frame_height\s*=\s*16", content)) or
            "vertical" in self.path.name.lower() or
            (self.path.parent / "manim_vertical.cfg").exists()
        ) and "16:9" not in content[:300] and "horizontal" not in self.path.name.lower()

        if not is_vertical:
            return

        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            if ".to_edge(" in line and ("UP" in line or "DOWN" in line):
                buff_match = re.search(r"buff\s*=\s*([0-9.]+)", line)
                if not buff_match:
                    self.findings.append((
                        "WARN", i,
                        "Safe Zone: 'to_edge(UP/DOWN)' uses default small buff (0.25). In 9:16 vertical video, platform UI may occlude text. Use buff >= 1.2 top, buff >= 1.5 bottom."
                    ))
                else:
                    buff_val = float(buff_match.group(1))
                    if "UP" in line and buff_val < 1.0:
                        self.findings.append((
                            "WARN", i,
                            f"Safe Zone: Top buff={buff_val} is small for 9:16 video. Recommend buff >= 1.2 to clear search bar / status UI."
                        ))
                    elif "DOWN" in line and buff_val < 1.2:
                        self.findings.append((
                            "WARN", i,
                            f"Safe Zone: Bottom buff={buff_val} is small for 9:16 video. Recommend buff >= 1.5 to clear captions & sound UI."
                        ))

    def _audit_scene_exits(self, content: str):
        """Checks if scenes end with clean exit transitions (FadeOut/wait)."""
        scene_blocks = re.findall(r"class\s+([A-Za-z0-9_]+)\s*\([^)]*Scene[^)]*\):([\s\S]*?)(?=\nclass|\Z)", content)
        for scene_name, block in scene_blocks:
            play_count = len(re.findall(r"\bself\.play\(", block))
            if play_count >= 2:
                # Check if FadeOut or clear exists
                has_exit = (
                    "FadeOut" in block or
                    "Uncreate" in block or
                    "self.wait" in block
                )
                if not has_exit:
                    self.findings.append((
                        "WARN", 0,
                        f"Clean Scene Exit: Scene '{scene_name}' does not appear to end with a FadeOut or pause."
                    ))

    def _print_report(self):
        fails = sum(1 for sev, _, _ in self.findings if sev == "FAIL")
        warns = sum(1 for sev, _, _ in self.findings if sev == "WARN")

        if self.json_mode:
            report_data = {
                "file": str(self.path),
                "filename": self.path.name,
                "status": "FAILED" if fails > 0 else ("PASSED_WITH_WARNINGS" if warns > 0 else "PASSED"),
                "critical_errors": fails,
                "warnings": warns,
                "findings": [
                    {"severity": sev, "line": line, "message": msg}
                    for sev, line, msg in self.findings
                ]
            }
            print(json.dumps(report_data, indent=2))
            return

        print("=" * 68)
        print(f" ANIMATHOR SCRIPT & CODE QUALITY AUDIT v2.0: {self.path.name}")
        print("=" * 68)
        if not self.findings:
            print("[+] PASS: 100% compliant with Anti-Slop, Accuracy & Pacing standards!")
            print("=" * 68)
            return

        for sev, line, msg in self.findings:
            loc = f"Line {line:3d}" if line > 0 else "Overall "
            tag = f"[{sev}]"
            print(f" {tag:6s} | {loc} | {msg}")

        print("-" * 68)
        status = "FAILED" if fails > 0 else "PASSED WITH WARNINGS"
        print(f"Result: {status} ({fails} critical errors, {warns} warnings)")
        print("=" * 68)


def main():
    parser = argparse.ArgumentParser(description="Animathor Script & Code Quality Validator v2.0")
    parser.add_argument("file", help="Path to storyboard markdown or python scene script")
    parser.add_argument("--json", action="store_true", help="Output findings in structured JSON format")
    args = parser.parse_args()

    validator = ScriptValidator(args.file, json_mode=args.json)
    success = validator.audit()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
