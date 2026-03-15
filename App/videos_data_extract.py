import os, json, re, csv
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("YOUTUBE_API_KEY")
watch_history_file = BASE_DIR / "watch history" / "watch_history.json"


def video_data_extract():
    if not watch_history_file.exists():
        print(f"Error: {watch_history_file} not found!")
        return pd.DataFrame(columns=["Video ID", "Watch Time"])

    with open(watch_history_file, "r", encoding="utf-8") as wh_file:
        data = json.load(wh_file)

    video_ids = []
    video_data = []
    for item in data:
        url = item.get("titleUrl", " ")
        match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
        if match:
            video_ids.append(match.group(1))
    with open("video_ids.txt", "w") as Ids_file:
        for vid in video_ids:
            Ids_file.write(f"{vid}\n")
    for item in data:
        url = item.get("titleUrl", "")
        time = item.get("time", "")
        match = re.search(r"(?:v=|shorts/)([a-zA-Z0-9_-]{11})", url)
        if match:
            video_id = match.group(1)
            video_data.append({"Video ID": video_id, "Watch Time": time})
    print(f"Extracted {len(video_data)} valid video IDs")
    return video_data_with_time(video_data)


def video_data_with_time(video_data):
    with open("video_ids_with_time.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Video ID", "Watch Time"])
        writer.writeheader()
        writer.writerows(video_data)
    ID_Time = pd.read_csv("video_ids_with_time.csv")
    ID_Time = ID_Time[ID_Time["Watch Time"].str.startswith("2025")].reset_index(
        drop=True
    )
    ID_Time = ID_Time.drop_duplicates(subset="Video ID").reset_index(drop=True)
    print(f"Found {len(ID_Time)} videos from 2025")
    return ID_Time
