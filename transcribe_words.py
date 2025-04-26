# Created by Antonio De Nuevo, 2025
#
# This script uses a machine learning model to transcribe a video into individual word segments.
# It saves each word as a separate video clip inside a folder, organized by word.
#
# It's the first one in the sequence. 

import os
import json
import tempfile
from moviepy.editor import VideoFileClip
from faster_whisper import WhisperModel


VIDEO_PATH = "video.mp4"
OUTPUT_JSON = "video.json"

# Load video and extract audio to a temporary WAV file
def extract_audio(video_path):
    clip = VideoFileClip(video_path)
    temp_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
    clip.audio.write_audiofile(temp_audio, codec="pcm_s16le")
    return temp_audio

# Transcribe audio and save word-level timing
def transcribe_words(audio_path):
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio_path, word_timestamps=True)

    words = []
    for segment in segments:
        for word in segment.words:
            words.append({
                "word": word.word,
                "start": word.start,
                "end": word.end
            })
    return words

def main():
    audio_path = extract_audio(VIDEO_PATH)
    words = transcribe_words(audio_path)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(words, f, indent=2)
    print(f"Saved {len(words)} words to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
