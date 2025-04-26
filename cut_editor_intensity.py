# Created by Antonio De Nuevo, 2025
#
# This script creates an edit based on the intensity levels exported from analyze_intensity
# 
# 

import os
import json
from pathlib import Path
from moviepy.editor import VideoFileClip, concatenate_videoclips

# --- Configuration ---
INTENSITY_PATH = "clip_intensity.json"
CUTS_FOLDER = "cuts"
OUTPUT_FILE = "mixtape_curve_supercut.mp4"

# --- Load intensity data ---
with open(INTENSITY_PATH, "r") as f:
    intensity_data = json.load(f)

# --- Filter and sort clips ---
usable_clips = [(fname, score) for fname, score in intensity_data.items() if score > 0]
usable_clips.sort(key=lambda x: x[1])  # sort by intensity

# --- Create intensity curve: quiet → loud → quiet ---
half = len(usable_clips) // 2
curve_sequence = usable_clips[:half] + usable_clips[:half][::-1]  # mirror the first half

# --- Load video clips ---
final_clips = []
for filename, _ in curve_sequence:
    word = filename.split("_")[0]
    clip_path = os.path.join(CUTS_FOLDER, word, filename)
    if os.path.exists(clip_path):
        try:
            clip = VideoFileClip(clip_path)
            final_clips.append(clip)
        except Exception as e:
            print(f"Skipping {clip_path} — {e}")
    else:
        print(f"Missing file: {clip_path}")

# --- Concatenate and export ---
if final_clips:
    final_video = concatenate_videoclips(final_clips, method="compose")
    final_video.write_videofile(OUTPUT_FILE, codec="libx264", audio_codec="aac")
    print(f"Saved curve-based supercut: {OUTPUT_FILE}")
else:
    print("NNo valid clips found.")
