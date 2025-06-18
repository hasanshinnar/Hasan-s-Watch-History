# 📊 YouTube Watch History Analyzer

A data analysis project that uses Python and Power BI to process your YouTube watch history, classify video types, track new channels, calculate time spent on Shorts, and more!

---

## 💡 Project Overview

This project parses your `watch-history.json` file (exported via Google Takeout), retrieves video metadata using the YouTube API, and outputs a clean Excel dataset ready for Power BI visualizations.

Key insights you can explore in Power BI:

- Total watch time by day/month
- Time spent on Shorts vs. regular videos
- New channels are discovered each month
- Most-watched channels
- Types of content you consume

---

## 📁 Project Structure

- `main.py` – Python script that extracts, cleans, and enriches video data
- `video_ids_with_time.csv` – Extracted video IDs and watch times
- `YouTube_2025_History.xlsx` – Final Excel dataset for Power BI
- `.env` – Environment file storing your YouTube API key (not included)
- `requirements.txt` – Required Python libraries

---

## ⚙️ How to Run

1. **Download your watch history** from [Google Takeout](https://takeout.google.com/) as a JSON file.
2. Place `watch-history.json` in the project root directory.
3. Create a `.env` file with your YouTube API key:
   ```env
   YOUTUBE_API_KEY=your_api_key_here

## ⚙️ Install dependencies:

pip install -r requirements.txt

## ⏯️ Run the script:

python main.py

## Once finished, open YouTube_2025_History.xlsx in Power BI and start building your dashboard!

## Examples of the final dashboard 

![Image](https://github.com/user-attachments/assets/3883f127-030c-4f78-b829-b564f79458fb)
![Image](https://github.com/user-attachments/assets/18db6ab8-dfaa-495c-8931-87bc2a506da8)

## 🙏 Thank You

Thank you for checking out this project! If you found it helpful or have suggestions for improvements, feel free to open an issue or contribute. Happy analyzing!
