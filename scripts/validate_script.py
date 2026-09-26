#!/usr/bin/env python3
"""
Animathor Script & Code Quality Validator (Anti-Slop & Accuracy Linter)
Audits storyboards (markdown) and animation scripts (python) against:
- Rule R-02: Zero Em Dashes (—)
- Anti-Slop: Banned AI clichés and marketing buzzwords
- Pacing Budget: Words-per-second speech constraints (<= 2.3 wps)
- Technical Integrity: LaTeX raw string escaping, monospace font usage, clean exits
"""

import sys
import re
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
]


class ScriptValidator:
    def __init__(self, filepath: str | Path):
        self.path = Path(filepath)
        self.findings: list[tuple[str, int, str]] = []  # (severity, line_num, message)

    def audit(self) -> bool:
        if not self.path.exists():
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
        # Return True if 0 FAIL findings
        has_critical = any(sev == "FAIL" for sev, _, _ in self.findings)
        return not has_critical

    def _audit_markdown(self, lines: list[str], content: str):
        # 1. Em Dash Check (Rule R-02)
        for i, line in enumerate(lines, 1):
            if "—" in line:
                self.findings.append(("FAIL", i, "Rule R-02: Em dash character ('—') detected. Use a comma, colon, or period."))
            if " – " in line:
                self.findings.append(("WARN", i, "En dash ('–') used as parenthetical separator. Replace with comma or colon."))

        # 2. Banned AI Buzzwords
        for i, line in enumerate(lines, 1):
            for pattern in BANNED_AI_WORDS:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    word = match.group(0)
                    self.findings.append(("FAIL", i, f"Anti-Slop: Banned AI cliché '{word}' detected. State the concept directly."))

        # 3. Exclamation Stuffing Check
        exclamations = content.count("!")
        if exclamations > 3:
            self.findings.append(("WARN", 0, f"Exclamation count ({exclamations}) is high. Aim for <= 2 in technical cinema."))

        # 4. Word Budget / Pacing Check in AV Tables
        # Matches patterns like: *(15 words • 1.2 wps)* or counts words between quotes in beats
        table_rows = re.findall(r"\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|", content)
        for row in table_rows:
            beat_info = row[0].strip()
            narration = row[3].strip()
            # Extract duration in seconds
            dur_match = re.search(r"(\d+)\s*(?:detik|seconds|sec|s)", beat_info, re.IGNORECASE)
            # Extract spoken text inside quotes
            speech_match = re.search(r'"(.*?)"', narration, re.DOTALL)
            if dur_match and speech_match:
                duration = float(dur_match.group(1))
                speech_text = speech_match.group(1).strip()
                words = len(speech_text.split())
                wps = words / duration if duration > 0 else 0
                if wps > 2.3:
                    self.findings.append((
                        "FAIL", 0,
                        f"Pacing Overload: Beat ({duration:.0f}s) has {words} words ({wps:.2f} words/sec). Max allowed is 2.3 wps."
                    ))

    def _audit_python(self, lines: list[str], content: str):
        # 1. Em Dash in Strings
        for i, line in enumerate(lines, 1):
            if "—" in line:
                self.findings.append(("FAIL", i, "Rule R-02: Em dash ('—') in Python string or comment."))

        # 2. Monospace Font Guard
        has_mono = re.search(r'MONO\s*=\s*["\'](Consolas|Menlo|DejaVu Sans Mono|Courier)', content)
        if not has_mono and "Scene" in content:
            self.findings.append(("FAIL", 0, "Pango Kerning Guard: No MONO font defined (must use Consolas, Menlo, or DejaVu Sans Mono)."))

        # 3. LaTeX Raw String Escaping
        for i, line in enumerate(lines, 1):
            bad_mathtex = re.search(r'MathTex\(\s*["\']\\[a-zA-Z]', line)
            bad_tex = re.search(r'Tex\(\s*["\']\\[a-zA-Z]', line)
            if bad_mathtex or bad_tex:
                self.findings.append(("FAIL", i, "LaTeX Syntax: MathTex/Tex string missing raw prefix r'...' or R'...'."))

        # 4. Banned Buzzwords in text strings
        for i, line in enumerate(lines, 1):
            for pattern in BANNED_AI_WORDS:
                if re.search(pattern, line, re.IGNORECASE):
                    self.findings.append(("WARN", i, f"Anti-Slop: Potential AI buzzword in line: {line.strip()[:60]}"))

    def _print_report(self):
        print("=" * 65)
        print(f" ANIMATHOR SCRIPT & CODE QUALITY AUDIT: {self.path.name}")
        print("=" * 65)
        if not self.findings:
            print("[+] PASS: 100% compliant with Anti-Slop, Accuracy & Pacing standards!")
            print("=" * 65)
            return

        fails = sum(1 for sev, _, _ in self.findings if sev == "FAIL")
        warns = sum(1 for sev, _, _ in self.findings if sev == "WARN")

        for sev, line, msg in self.findings:
            loc = f"Line {line:3d}" if line > 0 else "Overall "
            tag = f"[{sev}]"
            print(f" {tag:6s} | {loc} | {msg}")

        print("-" * 65)
        status = "FAILED" if fails > 0 else "PASSED WITH WARNINGS"
        print(f"Result: {status} ({fails} critical errors, {warns} warnings)")
        print("=" * 65)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_script.py <storyboard.md | script.py>")
        sys.exit(1)

    target = sys.argv[1]
    validator = ScriptValidator(target)
    success = validator.audit()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
