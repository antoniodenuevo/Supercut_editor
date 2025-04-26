# Created by Antonio De Nuevo, 2025
#
# This script analyses the intensity of the clips exported

import os
import json
from pathlib import Path
from pydub import AudioSegment
from moviepy.editor import VideoFileClip


# --- Configuration ---
ROOT_FOLDER = "cuts"  # Folder containing subfolders with clips
OUTPUT_FILE = "clip_intensity.json"

def get_audio_rms(video_path):
    """Extract audio and compute RMS using pydub."""
    try:
        video = VideoFileClip(str(video_path))
        audio_path = str(video_path).replace(".mp4", ".wav")
        video.audio.write_audiofile(audio_path, verbose=False, logger=None)
        audio = AudioSegment.from_file(audio_path)
        os.remove(audio_path)
        return audio.rms
    except Exception as e:
        print(f"Skipping {video_path.name} — audio error: {e}")
        return None

def main():
    results = {}
    root = Path(ROOT_FOLDER)
    for subfolder in sorted(root.iterdir()):
        if subfolder.is_dir():
            for video_file in sorted(subfolder.glob("*.mp4")):
                rms = get_audio_rms(video_file)
                if rms is not None:
                    results[video_file.name] = rms

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} entries to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
