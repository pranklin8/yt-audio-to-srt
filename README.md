# 🎬 YouTube to English SRT Generator

Generate English subtitle (`.srt`) files from YouTube videos using OpenAI Whisper.

The script:

- Downloads audio from a YouTube video
- Extracts and converts it to MP3
- Transcribes and translates speech to English
- Generates an SRT subtitle file

---

## Features

- YouTube audio downloading with `yt-dlp`
- Automatic speech recognition using Whisper
- Translation to English
- Standard SRT subtitle output
- Simple command-line interface

---

## Requirements

- Python 3.8+
- FFmpeg

### Python Packages

```bash
pip install yt-dlp openai-whisper torch
```

---

## Install FFmpeg

Verify FFmpeg is installed:

```bash
ffmpeg -version
```

If FFmpeg is not installed:

### Ubuntu / Debian

```bash
sudo apt install ffmpeg
```

### macOS

```bash
brew install ffmpeg
```

### Windows

Download and install from:

https://ffmpeg.org/download.html

Add FFmpeg to your system PATH.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-english-srt-generator.git
cd youtube-english-srt-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install yt-dlp openai-whisper torch
```

---

## Usage

Run the script:

```bash
python main.py
```

Enter a YouTube URL:

```text
Enter YouTube URL:
https://www.youtube.com/watch?v=VIDEO_ID
```

Example output:

```text
Downloading audio...
Loading Whisper model...
Transcribing and translating to English...
Saving SRT...
Done. Saved: translated_en.srt
```

---

## Output

Generated file:

```text
translated_en.srt
```

Example:

```srt
1
00:00:00,000 --> 00:00:03,500
Hello everyone.

2
00:00:03,500 --> 00:00:07,000
Welcome to today's presentation.
```

---

## Whisper Models

Current model:

```python
model = whisper.load_model("medium")
```

Available models:

- tiny
- base
- small
- medium
- large

For faster processing on low-end hardware:

```python
model = whisper.load_model("small")
```

For maximum accuracy:

```python
model = whisper.load_model("large")
```

---

## Project Workflow

```text
YouTube Video
      ↓
Download Audio
      ↓
Convert to MP3
      ↓
Whisper Translation
      ↓
Generate SRT
      ↓
translated_en.srt
```

---

## Notes

- Internet connection is required.
- FFmpeg must be installed and accessible from PATH.
- Processing time depends on video length and selected Whisper model.
- Translation quality depends on audio clarity.

---

## License

MIT License

---

## Acknowledgments

- OpenAI Whisper
- yt-dlp
- FFmpeg
- PyTorch
