# 🎬 YouTube → English Subtitle Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green)
![yt--dlp](https://img.shields.io/badge/yt--dlp-Latest-red)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

This project is a Python-based command-line utility that:

1. Downloads audio from a YouTube video.
2. Extracts and converts the audio to MP3 format.
3. Uses OpenAI Whisper to transcribe speech.
4. Translates detected speech into English.
5. Generates a standard `.srt` subtitle file.

The generated subtitle file can be used with media players, video editors, streaming platforms, and subtitle management tools.

---

# ✨ Features

## Audio Downloading

- Downloads audio directly from YouTube.
- Uses the best available audio quality.
- Supports a wide range of YouTube videos.

## Audio Conversion

- Automatically extracts audio using FFmpeg.
- Converts audio into MP3 format.
- Uses 192 kbps quality output.

## Speech Recognition

- Powered by OpenAI Whisper.
- Supports dozens of spoken languages.
- Automatically detects the source language.

## Translation

- Converts recognized speech into English.
- Uses Whisper's built-in translation capability.
- No separate translation API required.

## Subtitle Generation

- Generates valid SRT subtitle files.
- Includes accurate timestamps.
- Compatible with:
  - VLC
  - MPC-HC
  - PotPlayer
  - YouTube Studio
  - Adobe Premiere Pro
  - DaVinci Resolve
  - Final Cut Pro

## Automatic Cleanup

- Removes temporary audio files after processing.
- Keeps the workspace clean.

---

# 📂 Project Structure

```text
youtube-subtitle-generator/
│
├── main.py
├── README.md
└── translated_en.srt
```

---

# 🔧 Requirements

## Operating System

Supported operating systems:

- Windows
- Linux
- macOS

---

## Python Version

Minimum:

```text
Python 3.8
```

Recommended:

```text
Python 3.10+
```

Check your version:

```bash
python --version
```

---

# 📦 Dependencies

The project depends on the following packages:

| Package | Purpose |
|----------|----------|
| yt-dlp | Download YouTube audio |
| openai-whisper | Speech recognition and translation |
| torch | Deep learning backend |
| ffmpeg | Audio extraction and conversion |

---

# 🛠 Installing FFmpeg

FFmpeg is required.

---

## Windows

### Step 1

Download FFmpeg:

https://ffmpeg.org/download.html

or

https://www.gyan.dev/ffmpeg/builds/

### Step 2

Extract the downloaded archive.

Example:

```text
C:\ffmpeg
```

### Step 3

Locate:

```text
C:\ffmpeg\bin
```

### Step 4

Add the path to Environment Variables.

### Step 5

Verify installation:

```bash
ffmpeg -version
```

Expected:

```text
ffmpeg version ...
```

---

## Ubuntu / Debian

Install FFmpeg:

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

---

## Fedora

```bash
sudo dnf install ffmpeg
```

---

## Arch Linux

```bash
sudo pacman -S ffmpeg
```

---

## macOS

Using Homebrew:

```bash
brew install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

---

# 📥 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/youtube-subtitle-generator.git
```

Move into the project:

```bash
cd youtube-subtitle-generator
```

---

## Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Required Packages

```bash
pip install yt-dlp
pip install openai-whisper
pip install torch
```

or

```bash
pip install yt-dlp openai-whisper torch
```

---

# 🚀 Running the Program

Execute:

```bash
python main.py
```

You will see:

```text
Enter YouTube URL:
```

Paste a YouTube link:

```text
https://www.youtube.com/watch?v=xxxxxxxxxxx
```

Example:

```text
Downloading audio...
Loading Whisper model...
Transcribing and translating to English...
Saving SRT...
Done. Saved: translated_en.srt
```

---

# 🔍 Source Code Explanation

---

## Import Statements

```python
import os
import yt_dlp
import whisper
from datetime import timedelta
```

Purpose:

- `os` → file operations
- `yt_dlp` → YouTube downloading
- `whisper` → transcription and translation
- `timedelta` → timestamp formatting

---

# Function: format_timestamp()

```python
def format_timestamp(seconds):
```

Converts seconds into SRT timestamp format.

Example:

```python
12.345
```

Output:

```text
00:00:12,345
```

SRT requires:

```text
HH:MM:SS,mmm
```

Example:

```text
01:15:30,500
```

---

# Function: download_audio()

```python
def download_audio(youtube_url, output_file="audio"):
```

Downloads audio from YouTube.

Configuration:

```python
{
    "format": "bestaudio/best",
}
```

Meaning:

- Download highest-quality audio available.

---

### FFmpeg Postprocessor

```python
{
    "key": "FFmpegExtractAudio",
    "preferredcodec": "mp3",
    "preferredquality": "192",
}
```

Meaning:

- Convert to MP3.
- Use 192 kbps quality.

Output:

```text
audio.mp3
```

---

# Function: save_srt()

```python
def save_srt(segments, filename):
```

Creates the subtitle file.

Each subtitle contains:

```text
Subtitle Number
Start Time
End Time
Subtitle Text
```

Example:

```text
1
00:00:01,000 --> 00:00:04,000
Hello everyone.
```

---

# Function: generate_english_srt()

```python
def generate_english_srt(
    youtube_url,
    output_srt="translated_en.srt"
)
```

Main workflow.

Performs:

### Step 1

Download audio.

### Step 2

Load Whisper model.

### Step 3

Transcribe audio.

### Step 4

Translate to English.

### Step 5

Generate SRT.

### Step 6

Delete temporary audio.

### Step 7

Display completion message.

---

# 🧠 Whisper Model Information

Current code uses:

```python
model = whisper.load_model("medium")
```

---

## Available Models

| Model | Size | Speed | Accuracy |
|---------|---------|---------|---------|
| tiny | ~39 MB | Very Fast | Lowest |
| base | ~74 MB | Fast | Good |
| small | ~244 MB | Moderate | Better |
| medium | ~769 MB | Slower | High |
| large | ~1550 MB | Slowest | Best |

---

## Change Model

Example:

```python
model = whisper.load_model("small")
```

or

```python
model = whisper.load_model("large")
```

---

# ⚡ GPU Acceleration

Whisper supports NVIDIA CUDA.

Check GPU availability:

```python
import torch

print(torch.cuda.is_available())
```

Output:

```text
True
```

means GPU is available.

---

# 📄 Example Generated Subtitle

```srt
1
00:00:00,000 --> 00:00:03,500
Hello everyone.

2
00:00:03,500 --> 00:00:07,200
Welcome to today's lecture.

3
00:00:07,200 --> 00:00:10,100
We will discuss artificial intelligence.
```

---

# 🔄 Processing Pipeline

```text
YouTube URL
      │
      ▼
yt-dlp Download
      │
      ▼
FFmpeg MP3 Conversion
      │
      ▼
Whisper Model
      │
      ▼
Speech Recognition
      │
      ▼
Translation to English
      │
      ▼
Subtitle Segmentation
      │
      ▼
SRT Generation
      │
      ▼
translated_en.srt
```

---

# 🛠 Customization

## Change Subtitle Filename

Current:

```python
generate_english_srt(url)
```

Custom:

```python
generate_english_srt(
    url,
    output_srt="lecture.srt"
)
```

---

## Keep Downloaded Audio

Remove:

```python
os.remove(audio_file)
```

This preserves:

```text
audio.mp3
```

---

## Change Audio Quality

Current:

```python
"preferredquality": "192"
```

Alternatives:

```python
"preferredquality": "128"
```

```python
"preferredquality": "256"
```

```python
"preferredquality": "320"
```

---

# ⚠️ Limitations

- Requires internet access.
- Requires FFmpeg.
- Long videos may take significant processing time.
- Large Whisper models require more RAM.
- Translation quality depends on audio quality.
- Heavy background noise may reduce accuracy.
- Region-locked videos may not be downloadable.
- Private videos cannot be processed.

---

# 🐛 Troubleshooting

---

## FFmpeg Not Found

Error:

```text
ffmpeg not found
```

Solution:

Install FFmpeg and add it to PATH.

---

## Module Not Found

Error:

```text
ModuleNotFoundError
```

Solution:

```bash
pip install yt-dlp openai-whisper torch
```

---

## CUDA Out of Memory

Solution:

Use a smaller model.

Example:

```python
whisper.load_model("small")
```

or

```python
whisper.load_model("base")
```

---

## Slow Processing

Possible reasons:

- CPU-only execution
- Large model selected
- Long video duration

Use:

```python
whisper.load_model("small")
```

for faster processing.

---

# 🔒 Legal Notice

This software is provided for:

- Educational purposes
- Research
- Accessibility
- Personal use

Users are responsible for ensuring compliance with:

- Copyright laws
- YouTube Terms of Service
- Local regulations

Do not use the software to violate intellectual property rights.

---

# 📜 License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.

---

# 🙏 Acknowledgments

Special thanks to:

- OpenAI Whisper
- yt-dlp Contributors
- FFmpeg Developers
- PyTorch Team
- Python Community

---

# ⭐ Summary

This project provides a complete workflow for converting spoken content from YouTube videos into translated English subtitle files.

Workflow:

```text
YouTube Video
      ↓
Download Audio
      ↓
Convert to MP3
      ↓
Transcribe Speech
      ↓
Translate to English
      ↓
Generate SRT File
```

Output:

```text
translated_en.srt
```

Ready for use in video players, editors, and subtitle platforms.
