import json
import re
import csv
import isodate
import pandas as pd
import requests
import os
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()
os.chdir(r"C:\Users\PC\PycharmProjects\Watch History")
api_key = os.getenv("YOUTUBE_API_KEY")
watch_history_file = r"C:\Users\PC\PycharmProjects\Watch History\watch_history.json"

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
        video_data.append({
            "Video ID": video_id,
            "Watch Time": time
        })

print(f"Extracted {len(video_data)} valid video IDs")

with open("video_ids_with_time.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Video ID", "Watch Time"])
    writer.writeheader()
    writer.writerows(video_data)

ID_Time = pd.read_csv("video_ids_with_time.csv")
ID_Time = ID_Time[ID_Time["Watch Time"].str.startswith("2025")].reset_index(drop=True)
ID_Time = ID_Time.drop_duplicates(subset="Video ID").reset_index(drop=True)
print(f"Found {len(ID_Time)} videos from 2025")
results = []


for items in tqdm(range(0, len(ID_Time), 50), desc="Processing Batches"):
    batch = ID_Time.iloc[items:items+50]
    ids = ",".join(batch["Video ID"].tolist())
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,contentDetails",
        "id": ids,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    for item in data.get("items", []):
        video_id = item["id"]
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        published = item["snippet"]["publishedAt"]
        duration_raw = item["contentDetails"]["duration"]

        try:
            duration = str(isodate.parse_duration(duration_raw))
        except:
            duration = "Unknown"
        watch_time_row = ID_Time[ID_Time["Video ID"] == video_id]
        watch_time = watch_time_row["Watch Time"].values[0] if not watch_time_row.empty else "Unknown"

        results.append({
            "Video ID": video_id,
            "Title": title,
            "Channel": channel,
            "Duration": duration,
            "Published At": published,
            "Watch Time": watch_time
        })
#    print(f"Processed batch {items // 50 + 1}")

final = pd.DataFrame(results)
final.to_excel("YouTube_2025_History.xlsx", index=False)


print("File saved : YouTube_2025_History.xlsx ")