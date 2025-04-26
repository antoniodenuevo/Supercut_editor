# Created by Antonio De Nuevo, 2025
#
# This script cuts clips based on the json created by transcribe_words.py
# 
# 

import os
import json
from moviepy.editor import VideoFileClip
from collections import defaultdict
import string


# --- Configuration ---
VIDEO_PATH = "video.mp4"  
TRANSCRIPT_PATH = "video.json"  # Word-level transcript
OUTPUT_ROOT = "cuts"
PADDING_BEFORE = 0.2  # Seconds before word
PADDING_AFTER = 0.2   # Seconds after word
FADE_DURATION = 0.05   # Audio fade-in/out duration

# --- Load transcript ---
with open(TRANSCRIPT_PATH, "r") as f:
    transcript = json.load(f)

# --- Prepare output root ---
os.makedirs(OUTPUT_ROOT, exist_ok=True)
word_counters = defaultdict(int)

# --- Load video ---
video = VideoFileClip(VIDEO_PATH)

# --- Cut clips ---
for entry in transcript:
    raw_word = entry["word"]
    word = raw_word.strip().lower().strip(string.punctuation)

    if not word:
        continue

    start = max(0, entry["start"] - PADDING_BEFORE)
    end = min(video.duration, entry["end"] + PADDING_AFTER)

    folder = os.path.join(OUTPUT_ROOT, word)
    os.makedirs(folder, exist_ok=True)

    count = word_counters[word]
    filename = f"{word}_{count:04d}.mp4"
    path = os.path.join(folder, filename)

    print(f"Saving {path}")
    clip = video.subclip(start, end).audio_fadein(FADE_DURATION).audio_fadeout(FADE_DURATION)
    clip.write_videofile(path, codec="libx264", audio_codec="aac", verbose=False, logger=None)

    word_counters[word] += 1

print("All word clips saved.")
