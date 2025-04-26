# Supercut_editor

Antonio De Nuevo. 2025. All rights reserved.
 
This project explores video segmentation and reassembly using machine learning and generative techniques.

Starting with a source video, I use a speech-to-text model to generate a word-level transcript. Each word is then isolated into a separate video clip using precise timecodes.

## Workflow Overview

### 1. `transcribe_words.py`
Transcribes the video into word-level timestamps using a zero-shot object detection model.

### 2. `cut_words.py`
Cuts the original video into short clips for each transcribed word, organized into folders.

### 3. `word_counts.py`
Counts how many clips exist for each word — used to weight future generations.

---

## Path A: Generative Lyrics-Based Editing

### A1. `make_lyrics.py`
Uses GPT-2 to generate new "lyrics" based on available words and their frequency.

### A2. `cut_editor_lyrics.py`
Assembles a new video by selecting clips that match the generated words, using each clip only once.

---

## Path B: Audio Intensity-Based Editing

### B1. `analyze_intensity.py`
Measures the average volume of each clip and saves the results to a JSON file.

### B2. `cut_editor_intensity.py`
Builds a new video edit that curves from quiet to loud and back to quiet, using the intensity analysis.

---

## Output examples

Some examples of outputs of this program can be found in my website:
https://antoniodenuevo.com/project/supercuts

<img width="927" alt="site-screenshot" src="https://github.com/user-attachments/assets/5737f478-acbc-4794-aae0-6ef3959bb189" />




