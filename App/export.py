import pandas as pd


def export_to_csv(results, filename="exported_videos.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Exported {len(results)} videos to {filename}")
    print("File saved : YouTube_2025_History.xlsx ")
