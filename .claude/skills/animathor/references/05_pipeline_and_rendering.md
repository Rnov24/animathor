# 05. Pipeline, Rendering & Production Automation

This guide covers efficient rendering cycles, multi-scene concatenation, audio muxing, and troubleshooting.

---

## 1. CLI Rendering Presets & Workflow

### 1.1 Quality Flag Reference

| Flag | Resolution | FPS | Target Usage | Render Speed |
|---|---|---|---|---|
| `-ql` | $854 \times 480$ | 15 fps | Rapid development & timing checks | 5–15 sec / scene |
| `-qm` | $1280 \times 720$ | 30 fps | Mid-tier review & social drafts | 15–40 sec / scene |
| `-qh` | $1920 \times 1080$ | 60 fps | Production release (YouTube, Reels) | 45–120 sec / scene |
| `-qk` | $3840 \times 2160$ | 60 fps | Ultra-HD Master Archive | 2–5 min / scene |

### 1.2 Inspection Commands
```powershell
# Render single freeze frame as PNG (no video encoding overhead)
manim -s -ql script.py SceneName

# Automatically open output file upon completion
manim -pql script.py SceneName

# Render specific section from frame 100 to 200
manim -ql --skip_animations script.py SceneName
```

---

## 2. Multi-Scene Modular Pipeline

Never write an entire 5-minute video in a single monolithic `Scene` class. If an error occurs at minute 4, you must re-render the whole video.

### The Modular Pattern:
```python
class Scene1_Introduction(Scene):
    def construct(self):
        ...

class Scene2_CoreIntuition(Scene):
    def construct(self):
        ...

class Scene3_Resolution(Scene):
    def construct(self):
        ...
```

Render scenes independently:
```powershell
manim -qh script.py Scene1_Introduction Scene2_CoreIntuition Scene3_Resolution
```

---

## 3. Standard Directory Template & Local manim.cfg

Each project should be housed in its own self-contained directory containing:
```
my_project/
├── animathor.json     # Format, resolution, fps metadata
├── manim.cfg          # Local engine canvas presets
├── storyboard.md      # AV script
├── script.py          # Scene classes
├── assets/            # Audio, images, SVGs
└── output/            # Exported master videos
```

### 3.1 Why manim.cfg Matters
When `manim.cfg` is placed in the project root, running `manim script.py Scene1` automatically applies:
```ini
[CLI]
pixel_width = 1080
pixel_height = 1920
frame_rate = 60
background_color = #0B0F19
media_dir = ./media
```
This guarantees that resolution, orientation (portrait vs landscape), and background styling remain consistent regardless of who runs the command.

---

## 4. Stitching with ffmpeg

Create a `concat.txt` file listing all exported video clips:

```text
file 'media/videos/script/1080p60/Scene1_Introduction.mp4'
file 'media/videos/script/1080p60/Scene2_CoreIntuition.mp4'
file 'media/videos/script/1080p60/Scene3_Resolution.mp4'
```

Concatenate losslessly without re-encoding directly to `output/final.mp4`:
```powershell
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy output/final.mp4
```

Or run via the automated CLI:
```powershell
python scripts/animathor_cli.py stitch my_project/script.py
```

---

## 5. Voiceover & Audio Integration

### 4.1 Automated Voiceover via Edge-TTS
You can generate neural, studio-grade voices for free using `edge-tts`:

```powershell
# Neural English Voice (Male)
edge-tts --voice en-US-ChristopherNeural --text "Can smooth sine waves form a 90-degree corner?" --write-media scene1.mp3

# Neural English Voice (Female)
edge-tts --voice en-US-JennyNeural --text "Can smooth sine waves form a 90-degree corner?" --write-media scene1.mp3
```

### 4.2 Muxing Video and Audio
```powershell
ffmpeg -y -i final.mp4 -i voiceover.mp3 -c:v copy -c:a aac -shortest final_with_audio.mp4
```

---

## 5. Troubleshooting & Diagnostics

### 5.1 LaTeX Compilation Error (`latex error converting to dvi`)
- **Cause**: Unescaped backslashes or invalid LaTeX math syntax.
- **Fix**: Always prefix LaTeX strings with raw markers (`r"..."` in CE, `R"..."` in GL). Test formulas in simple math mode `$formula$`.

### 5.2 Letters Overlapping in Text (`Pango Kerning Bug`)
- **Cause**: Pango font engine calculating negative kerning offsets for variable-width fonts.
- **Fix**: Use monospace fonts: `Text("Your text", font="Consolas")`.

### 5.3 Mobject Disappears or Warps During Transform
- **Cause**: Attempting to animate an object before adding it or using `Transform` between mismatched VMobject types.
- **Fix**: Use `ReplacementTransform` or specify `path_arc=PI/2` to guide transformation paths smoothly.
