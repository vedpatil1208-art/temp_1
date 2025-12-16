import csv
import json
from datetime import datetime
import matplotlib.pyplot as plt

class DiaryEntry:
    def __init__(self, date, text, mood):
        self.date = date
        self.text = text
        self.mood = mood

    def to_dict(self):
        return {"date": self.date, "text": self.text, "mood": self.mood}


sentiment_score = lambda text: (
    "Happy" if "happy" in text.lower() or "good" in text.lower()
    else "Sad" if "sad" in text.lower()
    else "Angry" if "angry" in text.lower()
    else "Neutral"
)


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def analyze_sentiment(date, text):
    if not text.strip():
        raise ValueError("Diary entry cannot be empty")
    mood = sentiment_score(text)
    return DiaryEntry(date, text, mood)


def save_diary(entry):
    with open("diary_entries.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "text", "mood"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(entry.to_dict())


entries = []

while True:
    date = input("Enter date (YYYY-MM-DD) or exit: ")

    if date.lower() == "exit":
        break

    if not validate_date(date):
        print("Invalid date. Enter date in YYYY-MM-DD format")
        continue

    text = input("Write your diary entry: ")

    try:
        entry = analyze_sentiment(date, text)
        save_diary(entry)
        entries.append(entry)
        print("Saved mood:", entry.mood)
    except ValueError as e:
        print(e)


if entries:
    mood_counts = {}
    for entry in entries:
        mood_counts[entry.mood] = mood_counts.get(entry.mood, 0) + 1

    with open("mood_summary.json", "w") as file:
        json.dump(mood_counts, file, indent=4)

    plt.figure()
    plt.pie(mood_counts.values(), labels=mood_counts.keys(), autopct="%1.1f%%")
    plt.title("Emotion Pie Chart")
    plt.show()
