# Created by Antonio De Nuevo, 2025
#
# This script generates the lyrics randomly, I used GPT-2 before but it was hard for the model to stick to my words. literally.
# 

import json
import random


# Load word counts
with open("word_counts.json", "r") as f:
    word_counts = json.load(f)

# Create a flat list with repeated words based on frequency
word_list = []
for word, count in word_counts.items():
    word_list.extend([word] * count)

# Shuffle the list to create a "remixed" version
random.shuffle(word_list)

# Save the new sequence to a JSON file
with open("generated_sequence.json", "w") as f:
    json.dump(word_list, f, indent=2)

print("Word sequence saved to generated_sequence.json")
