import time
import random

# Sample texts for typing test
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is a measure of how fast a person can type.",
    "Practice makes perfect. Keep typing and improve speed.",
    "Python programming is fun and powerful."
]

# Select a random text
sample = random.choice(sample_texts)
print("\nType the following text as fast as you can:\n")
print(sample)
input("Press Enter to start...")

# Start time
start_time = time.time()

# User input
typed_text = input("\nStart typing: ")

# End time
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time
words_typed = len(typed_text.split())

# Calculate WPM
wpm = (words_typed / time_taken) * 60

# Calculate Accuracy
correct_words = sum(1 for a, b in zip(typed_text.split(), sample.split()) if a == b)
accuracy = (correct_words / len(sample.split())) * 100

# Display results
print(f"\nTyping Speed: {wpm:.2f} WPM")


