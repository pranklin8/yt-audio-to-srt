import os
import yt_dlp
import whisper
from datetime import timedelta


def format_timestamp(seconds):
    td = timedelta(seconds=float(seconds))

    total_seconds = int(td.total_seconds())
    milliseconds = int((seconds - total_seconds) * 1000)

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"


def download_audio(youtube_url, output_file="audio"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_file,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return output_file + ".mp3"


def save_srt(segments, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, start=1):
            start = format_timestamp(segment["start"])
            end = format_timestamp(segment["end"])
            text = segment["text"].strip()

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")


def generate_english_srt(youtube_url, output_srt="translated_en.srt"):
    print("Downloading audio...")
    audio_file = download_audio(youtube_url)

    print("Loading Whisper model...")
    model = whisper.load_model("medium")

    print("Transcribing and translating to English...")
    result = model.transcribe(
        audio_file,
        task="translate"
    )

    print("Saving SRT...")
    save_srt(result["segments"], output_srt)

    os.remove(audio_file)

    print(f"Done. Saved: {output_srt}")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    generate_english_srt(url)