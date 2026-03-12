import os, json, re
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("YOUTUBE_API_KEY")
watch_history_file = BASE_DIR / "App" / "Requierments" / "watch_history.json"

if watch_history_file.exists():
    with open(watch_history_file, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    print(f"Error: {watch_history_file} not found!")
    data = []

with open(watch_history_file, "r", encoding="utf-8") as WatchHistroy:
    data = json.load(WatchHistroy)
video_ids = []
video_data = []
for item in data:
    url = item.get("titleUrl", " ")
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    if match:
        video_ids.append(match.group(1))
with open("video_ids.txt", "w") as WatchHistroy:
    for vid in video_ids:
        WatchHistroy.write(f"{vid}\n")

for item in data:
    url = item.get("titleUrl", "")
    time = item.get("time", "")

    match = re.search(r"(?:v=|shorts/)([a-zA-Z0-9_-]{11})", url)
    if match:
        video_id = match.group(1)
        video_data.append({"Video ID": video_id, "Watch Time": time})

print(f"Extracted {len(video_data)} valid video IDs")
