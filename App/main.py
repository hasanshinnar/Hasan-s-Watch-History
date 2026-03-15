from App.videos_data_extract import video_data_extract
import isodate, requests
from tqdm import tqdm
from App import api_key, export


def main():
    ID_Time = video_data_extract()
    results = []

    for items in tqdm(range(0, len(ID_Time), 50), desc="Processing Batches"):
        batch = ID_Time.iloc[items : items + 50]
        ids = ",".join(batch["Video ID"].tolist())
        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {"part": "snippet,contentDetails", "id": ids, "key": api_key}
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
            watch_time = (
                watch_time_row["Watch Time"].values[0]
                if not watch_time_row.empty
                else "Unknown"
            )

        results.append(
            {
                "Video ID": video_id,
                "Title": title,
                "Channel": channel,
                "Duration": duration,
                "Published At": published,
                "Watch Time": watch_time,
            }
        )
    export.export_to_csv(results)


if __name__ == "__main__":
    main()
