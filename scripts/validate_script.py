#!/usr/bin/env python3
"""
Animathor Script & Code Quality Validator (Anti-Slop & Accuracy Linter v2.2)
Audits storyboards (markdown) and animation scripts (python) against:
- Rule R-02: Zero Em Dashes (Unicode U+2014)
- Rule R-03: Zero On-Screen Paragraphs (<= 6 words for canvas Text, no wall of text)
- Rule R-04: Zero Freak Subtitles / Meta-Prefixes (No 'Title:', 'Subtitle:', 'Beat X:', 'X: explain Y')
- Spatial Anti-Collision: Visual focal point protection & no blind stacking of text
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

        # 5. Dynamic AV Table Pacing & Word Budget Scanner + Freak Subtitle Guard
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
        onscreen_idx = -1

        for idx, col in enumerate(header_cols):
            if any(k in col for k in ["beat", "durasi", "duration", "time", "waktu"]):
                if beat_idx == -1:
                    beat_idx = idx
            if any(k in col for k in ["narasi", "narration", "voiceover", "spoken", "speech", "audio", "naskah"]):
                if narration_idx == -1:
                    narration_idx = idx
            if any(k in col for k in ["layar", "screen", "onscreen", "mathtex", "subtitle", "teks"]):
                if onscreen_idx == -1:
                    onscreen_idx = idx

        # Fallback column heuristics if headers differ
        if beat_idx == -1:
            beat_idx = 0
        if narration_idx == -1 and len(header_cols) >= 4:
            narration_idx = 3
        if onscreen_idx == -1 and len(header_cols) >= 5:
            onscreen_idx = 4

        # Process data rows (skip header and delimiter at index 0 and 1)
        for line_num, row_raw in table_lines[2:]:
            cols = [c.strip() for c in row_raw.strip("|").split("|")]
            if len(cols) <= max(beat_idx, narration_idx):
                continue

            beat_cell = cols[beat_idx]
            narration_cell = cols[narration_idx]

            # 1. Extract duration
            duration = self._extract_duration(beat_cell)
            if duration and duration > 0:
                # 2. Extract spoken text
                words_count = self._extract_spoken_word_count(narration_cell)
                if words_count > 0:
                    wps = words_count / duration
                    if wps > 2.3:
                        self.findings.append((
                            "FAIL", line_num,
                            f"Pacing Overload: Beat ({duration:.1f}s) has {words_count} words ({wps:.2f} words/sec). Max allowed is 2.3 wps."
                        ))

            # 3. Audit On-Screen Column (Rule R-03 and R-04)
            if onscreen_idx != -1 and len(cols) > onscreen_idx:
                screen_cell = cols[onscreen_idx]
                # Check for freak subtitle prefixes: **Subtitle**: ..., **Title**: ...
                if re.search(r'\*\*(?:Title|Subtitle|Headline|Caption|Explanation|Note|Beat\s*\d+)\*\*:\s*', screen_cell, re.IGNORECASE) or \
                   re.search(r'\b\w+\s*:\s*(?:explain|explaining|explains|shows|showing)\b', screen_cell, re.IGNORECASE):
                    self.findings.append((
                        "FAIL", line_num,
                        "Rule R-04 (Freak Subtitle): On-screen column contains robotic metadata prefix (e.g. '**Subtitle**:', '**Title**:', 'X: explain Y'). Keep on-screen labels clean."
                    ))

                # Check for on-screen paragraph wordiness
                # Strip out math formulas $...$ and mobject descriptors like title:
                cleaned_screen = re.sub(r"\$.*?\$", "", screen_cell)
                cleaned_screen = re.sub(r"`.*?`", "", cleaned_screen)
                cleaned_screen = re.sub(r"\b(title|eq|curve|badge|note|target)\s*:\s*", "", cleaned_screen, flags=re.IGNORECASE)
                screen_words = [w for w in re.split(r"\s+", cleaned_screen.strip()) if len(w) > 1 and not w.startswith("|")]
                if len(screen_words) > 8:
                    self.findings.append((
                        "WARN", line_num,
                        f"Rule R-03 (On-Screen Wordiness): On-screen column has {len(screen_words)} words. Keep on-screen labels <= 6 words; explanations belong in voiceover."
                    ))

    def _extract_duration(self, text: str) -> float | None:
        """Extracts seconds from timecodes or duration labels."""
        sec_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:detik|seconds|sec|s\b)", text, re.IGNORECASE)
        if sec_match:
            return float(sec_match.group(1))

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
        quote_match = re.search(r'["\'“«]([^"\'”»]{3,})["\'”»]', text, re.DOTALL)
        if quote_match:
            spoken_text = quote_match.group(1)
            words = [w for w in re.split(r"\s+", spoken_text.strip()) if w]
            return len(words)

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

        # 5. Rule R-03: Zero On-Screen Paragraphs (6-Word Ceiling)
        self._audit_onscreen_text_length(lines)

        # 6. Rule R-04: Zero Freak Subtitles / Meta-Prefixes
        self._audit_freak_subtitles(lines)

        # 7. Spatial Anti-Collision & Stacking Guard
        self._audit_spatial_collision(content)

        # 8. Visual Breathing Room Guard (self.wait >= 1.5s after major reveals)
        self._audit_breathing_room(content)

        # 9. Safe Zone Buffers for 9:16 Vertical Video
        self._audit_vertical_safe_zones(lines, content)

        # 10. Clean Scene Exit Guard
        self._audit_scene_exits(content)

    def _audit_onscreen_text_length(self, lines: list[str]):
        """Rule R-03: Ensures on-screen Text mobjects do not contain walls of explanatory text."""
        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            # Matches Text("...") or Paragraph("...")
            text_matches = re.finditer(r'\b(?:Text|Paragraph)\(\s*([rR]?["\'])([\s\S]*?)\1', line)
            for m in text_matches:
                raw_text = m.group(2).strip()
                # Skip font constants, color strings, or short abbreviations
                if not raw_text or raw_text in ["Consolas", "Menlo", "DejaVu Sans Mono"]:
                    continue
                words = [w for w in re.split(r"\s+", raw_text) if w]
                # If text exceeds 6 words, or contains multiple full sentences
                has_multisentence = bool(re.search(r'\.\s+[A-Z]', raw_text))
                if len(words) > 6 or (len(words) > 4 and has_multisentence):
                    preview = raw_text[:40] + "..." if len(raw_text) > 40 else raw_text
                    self.findings.append((
                        "FAIL", i,
                        f"Rule R-03 (On-Screen Paragraph): Text(...) contains {len(words)} words ('{preview}'). Canvas text must be a concise label (<= 6 words). Move explanations to spoken voiceover!"
                    ))

    def _audit_freak_subtitles(self, lines: list[str]):
        """Rule R-04: Detects robotic metadata prefixes or 'X: explain Y' patterns in Text()."""
        prefix_pattern = re.compile(
            r'\b(?:Text|Paragraph)\(\s*([rR]?["\'])\s*(?:Title|Subtitle|Headline|Caption|Label|Note|Explanation|Beat\s*\d+)\s*:',
            re.IGNORECASE
        )
        colon_explain_pattern = re.compile(
            r'\b(?:Text|Paragraph)\(\s*([rR]?["\'])[^:"\']{3,25}\s*:\s*(?:explain|explaining|explains|shows|showing|visualizes|here we)\b',
            re.IGNORECASE
        )

        for i, line in enumerate(lines, 1):
            if is_suppressed(line):
                continue
            if prefix_pattern.search(line):
                self.findings.append((
                    "FAIL", i,
                    "Rule R-04 (Freak Subtitle): On-screen text contains robotic metadata prefix ('Title:', 'Subtitle:', 'Explanation:'). Keep on-screen text clean and direct."
                ))
            elif colon_explain_pattern.search(line):
                self.findings.append((
                    "FAIL", i,
                    "Rule R-04 (Freak Subtitle): On-screen text contains 'X: explain Y' pattern. Replace with punchy standalone title or mathematical tag."
                ))

    def _audit_spatial_collision(self, content: str):
        """Detects blind stacking where new text is animated to an edge while previous text was not cleared."""
        scene_blocks = re.findall(r"class\s+([A-Za-z0-9_]+)\s*\([^)]*Scene[^)]*\):([\s\S]*?)(?=\nclass|\Z)", content)
        for scene_name, block in scene_blocks:
            lines = block.splitlines()
            edge_assignments: dict[str, list[str]] = {"UP": [], "DOWN": []}

            for line in lines:
                if is_suppressed(line):
                    continue
                # Track assignments to edges: title.to_edge(UP)
                up_match = re.search(r'([a-zA-Z_0-9]+)\.to_edge\(\s*UP', line)
                if up_match:
                    var_name = up_match.group(1)
                    if var_name not in edge_assignments["UP"]:
                        edge_assignments["UP"].append(var_name)

                down_match = re.search(r'([a-zA-Z_0-9]+)\.to_edge\(\s*DOWN', line)
                if down_match:
                    var_name = down_match.group(1)
                    if var_name not in edge_assignments["DOWN"]:
                        edge_assignments["DOWN"].append(var_name)

            # Check if multiple variables share UP or DOWN and neither FadeOut nor ReplacementTransform was used
            for edge, vars_list in edge_assignments.items():
                if len(vars_list) >= 2:
                    has_transform = "ReplacementTransform" in block or "Transform" in block
                    has_fadeout = "FadeOut" in block
                    if not (has_transform or has_fadeout):
                        self.findings.append((
                            "WARN", 0,
                            f"Spatial Collision Risk: Multiple objects {vars_list} placed at to_edge({edge}) in Scene '{scene_name}' without detected FadeOut or ReplacementTransform."
                        ))

    def _audit_breathing_room(self, content: str):
        """Verifies that scene animations include necessary viewer breathing pauses."""
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
        print(f" ANIMATHOR SCRIPT & CODE QUALITY AUDIT v2.2: {self.path.name}")
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
    parser = argparse.ArgumentParser(description="Animathor Script & Code Quality Validator v2.2")
    parser.add_argument("file", help="Path to storyboard markdown or python scene script")
    parser.add_argument("--json", action="store_true", help="Output findings in structured JSON format")
    args = parser.parse_args()

    validator = ScriptValidator(args.file, json_mode=args.json)
    success = validator.audit()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
