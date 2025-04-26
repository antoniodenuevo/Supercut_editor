# Created by Antonio De Nuevo, 2025
#
# This exports a list of all the words the appear in the song
#

import json
import string
from collections import defaultdict


# Load transcript
with open("video.json", "r") as f:
    transcript = json.load(f)

# Count words
counts = defaultdict(int)
for entry in transcript:
    word = entry["word"].strip().lower().strip(string.punctuation)
    if word:
        counts[word] += 1

# Sort alphabetically (optional)
counts_sorted = dict(sorted(counts.items()))

# Save to JSON
with open("word_counts.json", "w") as f:
    json.dump(counts_sorted, f, indent=2)

print("Saved word_counts.json")
