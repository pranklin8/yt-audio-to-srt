<div align="center">

# 🎬 YT Audio to SRT

### Generate English Subtitles from YouTube Videos using OpenAI Whisper

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/OpenAI-Whisper-10A37F?style=for-the-badge">
  <img src="https://img.shields.io/badge/yt--dlp-Latest-FF0000?style=for-the-badge">
  <img src="https://img.shields.io/badge/FFmpeg-Required-007808?style=for-the-badge">
</p>

<p>
  Download YouTube audio, translate speech to English, and generate ready-to-use SRT subtitle files automatically.
</p>

</div>

---

## ✨ Features

✅ Download audio directly from YouTube

✅ Convert audio to MP3 using FFmpeg

✅ Automatic speech recognition with Whisper

✅ Translate speech into English

✅ Generate standard `.srt` subtitle files

✅ Supports multiple spoken languages

✅ Simple and lightweight CLI tool

---

## 🔄 Workflow

```text
┌─────────────────────┐
│   YouTube Video     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Download Audio      │
│      (yt-dlp)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Convert to MP3      │
│      (FFmpeg)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Whisper Transcribe  │
│   + Translation     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Generate SRT File   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ translated_en.srt   │
└─────────────────────┘
```

---

## 📋 Requirements

| Requirement | Version |
|------------|---------|
| Python | 3.8+ |
| FFmpeg | Latest |
| yt-dlp | Latest |
| Whisper | Latest |
| PyTorch | Latest |

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pranklin8/yt-audio-to-srt.git
cd yt-audio-to-srt
```

### 2️⃣ Install Dependencies

```bash
pip install yt-dlp openai-whisper torch
```

---

## 🎥 Install FFmpeg

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

### macOS

```bash
brew install ffmpeg
```

### Windows

Download:

🔗 https://ffmpeg.org/download.html

Add FFmpeg to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

---

## 🚀 Usage

Run the application:

```bash
python main.py
```

Enter a YouTube URL:

```text
Enter YouTube URL:
https://www.youtube.com/watch?v=VIDEO_ID
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

## 📄 Output Example

Generated file:

```text
translated_en.srt
```

Example subtitle:

```srt
1
00:00:00,000 --> 00:00:03,500
Hello everyone.

2
00:00:03,500 --> 00:00:07,000
Welcome to today's presentation.
```

---

## 🧠 Whisper Models

Current model:

```python
model = whisper.load_model("medium")
```

Available models:

| Model | Speed | Accuracy |
|---------|---------|---------|
| tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ |
| base | ⚡⚡⚡⚡ | ⭐⭐⭐ |
| small | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| medium | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| large | ⚡ | ⭐⭐⭐⭐⭐⭐ |

Example:

```python
model = whisper.load_model("small")
```

---

## 📂 Project Structure

```text
yt-audio-to-srt/
│
├── main.py
├── README.md
└── translated_en.srt
```

---

## 🛠 Tech Stack

- 🐍 Python
- 🎙 OpenAI Whisper
- 📥 yt-dlp
- 🎵 FFmpeg
- 🔥 PyTorch

---

## ⚠️ Notes

- Internet connection is required for downloading model.
- FFmpeg must be installed.
- Processing time depends on video length.
- Larger Whisper models provide better accuracy but require more resources.

---

## 🙌 Credits

- OpenAI Whisper
- yt-dlp
- FFmpeg
- PyTorch

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star!

🔗 https://github.com/pranklin8/yt-audio-to-srt

</div>
