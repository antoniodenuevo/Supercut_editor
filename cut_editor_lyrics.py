# Created by Antonio De Nuevo, 2025
#
# This script creates an edit based on the new lyrics created by lyric_maker
# 
# 


import os
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

# this one creates a supercut using the lyrics from lyric_maker.py

# --- Configuration ---
CUTS_FOLDER = "cuts"  # Root folder where each word's folder lives
SEQUENCE_JSON = "generated_sequence.json"  # JSON file with new word sequence
OUTPUT_VIDEO = "supercut-name.mp4"
VIDEO_SIZE = (1920, 1080)  # Resize output if needed, or set to None
FPS = 30

# --- Load word sequence ---
with open(SEQUENCE_JSON, "r") as f:
    word_sequence = json.load(f)["words"]

# --- Build word -> list of available clips ---
available_clips = {}
for word in set(word_sequence):
    folder = os.path.join(CUTS_FOLDER, word)
    if not os.path.isdir(folder):
        print(f"⚠️ No folder found for word '{word}'")
        available_clips[word] = []
        continue
    files = sorted([
        os.path.join(folder, f) for f in os.listdir(folder)
        if f.lower().endswith(".mp4")
    ])
    available_clips[word] = files

# --- Build video sequence ---
final_clips = []
for word in word_sequence:
    clips = available_clips.get(word, [])
    if not clips:
        print(f"No clips left for word '{word}'")
        continue

    clip_path = clips.pop(0)
    available_clips[word] = clips  # Update list after popping

    print(f"Using '{clip_path}' for word '{word}'")
    clip = VideoFileClip(clip_path)

    # Resize if needed
    if VIDEO_SIZE:
        clip = clip.resize(newsize=VIDEO_SIZE)

    final_clips.append(clip)

# --- Save final video ---
if final_clips:
    final = concatenate_videoclips(final_clips, method="compose")
    final.write_videofile(OUTPUT_VIDEO, codec="libx264", audio_codec="aac", fps=FPS)
    print("🎬 Supercut saved as", OUTPUT_VIDEO)
else:
    print("❌ No clips to compile.")
