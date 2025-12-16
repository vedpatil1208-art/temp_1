import csv
import json
import matplotlib.pyplot as plt
from datetime import datetime

class DiaryEntry:
    def __init__(self, date_value, text):
        self.date = date_value
        self.text = text
        self.mood = self.analyze_sentiment()

    def analyze_sentiment(self):
        positive = ["happy", "good", "great", "excited", "love"]
        negative = ["sad", "bad", "angry", "upset", "hate"]
        score = sum(1 for w in positive if w in self.text.lower()) - sum(1 for w in negative if w in self.text.lower())
        return "Happy" if score > 0 else "Sad" if score < 0 else "Neutral"

    def save_diary(self):
        with open("diary_entries.csv", "a", newline="") as f:
            csv.writer(f).writerow([self.date, self.text, self.mood])

def valid_date(date_value):
    date_value = date_value.strip().replace("–", "-").replace("—", "-")
    if any(c.isalpha() for c in date_value):
        return False
    try:
        datetime.strptime(date_value, "%Y-%m-%d")
        return True
    except:
        return False

def load_entries():
    entries = []
    try:
        with open("diary_entries.csv", "r") as f:
            for row in csv.reader(f):
                if len(row) == 3:
                    entries.append(row[2])
    except FileNotFoundError:
        pass
    return entries

def save_summary(moods):
    summary = {"Happy": 0, "Sad": 0, "Neutral": 0}
    for m in moods:
        if m in summary:
            summary[m] += 1
    with open("mood_summary.json", "w") as f:
        json.dump(summary, f)
    return summary

def plot_pie(summary):
    labels = []
    values = []
    for k, v in summary.items():
        if v > 0:
            labels.append(k)
            values.append(v)
    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Emotion Distribution")
    plt.axis("equal")
    plt.show()

while True:
    date_input = input("Enter date (YYYY-MM-DD) or type exit: ")
    if date_input.lower() == "exit":
        break
    if not valid_date(date_input):
        print("Invalid date. Use YYYY-MM-DD with numbers only.")
        continue
    text_input = input("Enter diary entry: ")
    entry = DiaryEntry(date_input, text_input)
    entry.save_diary()

moods = load_entries()
summary = save_summary(moods)
plot_pie(summary)
