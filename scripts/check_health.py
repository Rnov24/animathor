#!/usr/bin/env python3
"""
Animathor Health Check Script
Verifies all dependencies, CLI tools, LaTeX engines, and ffmpeg for Manim development.
"""

import sys
import shutil
import subprocess
import importlib


def check_mark(success: bool) -> str:
    return "[OK]" if success else "[MISSING]"


def run_cmd(cmd: list[str]) -> tuple[bool, str]:
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if proc.returncode == 0:
            output = proc.stdout.strip().splitlines()
            return True, output[0] if output else "Available"
        return False, proc.stderr.strip().splitlines()[0] if proc.stderr else "Error"
    except Exception as e:
        return False, str(e)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=" * 60)
    print(" ANIMATHOR STUDIO - SYSTEM HEALTH & TOOLCHAIN CHECK")
    print("=" * 60)

    # 1. Python Version
    py_ver = sys.version_info
    py_ok = (py_ver.major == 3 and py_ver.minor >= 10)
    print(f"{check_mark(py_ok)} Python: {py_ver.major}.{py_ver.minor}.{py_ver.micro} (Requires >= 3.10)")

    # 2. Core Packages
    packages = [
        ("manim", "Manim Community Edition (ManimCE)"),
        ("manimlib", "ManimGL (3b1b OpenGL version, optional)"),
        ("numpy", "NumPy Numerical Computing"),
        ("scipy", "SciPy Scientific Library"),
        ("edge_tts", "Edge-TTS Neural Voiceover (optional)"),
    ]

    print("\n[Python Libraries]")
    for mod_name, desc in packages:
        try:
            mod = importlib.import_module(mod_name)
            ver = getattr(mod, "__version__", "Available")
            print(f"  {check_mark(True)} {desc}: v{ver}")
        except ImportError:
            is_optional = "optional" in desc
            tag = "[INFO]" if is_optional else "[MISSING]"
            print(f"  {tag} {desc}: Not Installed")

    # 3. System CLI Binaries
    print("\n[External CLI Toolchain]")
    binaries = [
        ("ffmpeg", ["ffmpeg", "-version"], "FFmpeg Video Encoder/Stitcher"),
        ("latex", ["latex", "--version"], "LaTeX Compiler (MathTex support)"),
        ("dvisvgm", ["dvisvgm", "--version"], "DVI-to-SVG Vector Converter"),
    ]

    for bin_name, test_cmd, desc in binaries:
        path = shutil.which(bin_name)
        if path:
            ok, ver_info = run_cmd(test_cmd)
            print(f"  {check_mark(True)} {desc}: {ver_info} ({path})")
        else:
            print(f"  {check_mark(False)} {desc}: Not found in system PATH")

    print("\n" + "=" * 60)
    print("Health check completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
