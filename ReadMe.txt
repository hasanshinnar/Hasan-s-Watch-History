# YouTube Watch History Analyzer

This project analyzes my YouTube watch history using Python, YouTube Data API, and Power BI.

## Features
- Extracts video IDs and watch time from YouTube history
- Fetches metadata (title, channel, duration, etc.)
- Filters 2025 videos only
- Exports data to Excel for Power BI visualization

## How to run
1. Put your `watch_history.json` file in the root folder
2. Add your API key to `.env` as `YOUTUBE_API_KEY=your_key_here`
3. Run `main.py`

## Requirements
See `requirements.txt`