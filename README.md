# YouTube Watch History Analyzer !!! The code is under maintenance !!!

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![YouTube API](https://img.shields.io/badge/YouTube-Data%20API%20v3-red.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow.svg)

A powerful Python tool that transforms your YouTube watch history into actionable insights using data analytics and visualization.

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) 

</div>

---

## Overview

YouTube Watch History Analyzer is a comprehensive data analysis tool that processes your YouTube watch history, enriches it with video metadata through the YouTube Data API, and prepares structured datasets for visualization in Power BI. Gain insights into your viewing patterns, favorite channels, content preferences, and time spent on the platform.

## Features

- **Data Extraction**: Parses YouTube's native `watch_history.json` export file
- **Metadata Enrichment**: Fetches comprehensive video details via YouTube Data API v3
  - Video titles and descriptions
  - Channel information
  - Video duration and categories
  - Publication dates
  - View counts and engagement metrics
- **Smart Filtering**: Isolates videos watched in 2025 (configurable)
- **Excel Export**: Generates clean, structured datasets optimized for Power BI
- **Batch Processing**: Efficiently handles large watch histories with API quota management
- **Error Handling**: Robust error management for API limits and network issues

## Demo

<div align="center">

### Dashboard Overview
![Dashboard Screenshot 1](https://github.com/user-attachments/assets/3883f127-030c-4f78-b829-b564f79458fb)

### Detailed Analytics
![Dashboard Screenshot 2](https://github.com/user-attachments/assets/18db6ab8-dfaa-495c-8931-87bc2a506da8)

</div>

## Installation

### Prerequisites

- Python 3.8 or higher
- YouTube Data API v3 key ([Get one here](https://console.cloud.google.com/apis/credentials))
- Your YouTube watch history JSON file ([Download from Google Takeout](https://takeout.google.com/))

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/youtube-watch-history-analyzer.git
   cd youtube-watch-history-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your YouTube API key:
   ```env
   YOUTUBE_API_KEY=your_api_key_here
   ```

4. **Add your watch history**
   
   Place your `watch_history.json` file in the project root directory.

## Usage

### Basic Usage

Run the analyzer with default settings:

```bash
python main.py
```

This will:
1. Load your watch history
2. Extract video IDs and timestamps
3. Fetch metadata from YouTube API
4. Filter for 2025 videos
5. Export results to `output/youtube_analysis.xlsx`

### Advanced Configuration

<<<<<<< HEAD
Customize the analysis by modifying parameters in `config.py`:

```python
# Filter by year
TARGET_YEAR = 2025

# Output file location
OUTPUT_PATH = "output/youtube_analysis.xlsx"

# API batch size (adjust based on quota)
BATCH_SIZE = 50
```

### Output Structure

The generated Excel file contains the following columns:

| Column | Description |
|--------|-------------|
| `video_id` | Unique YouTube video identifier |
| `title` | Video title |
| `channel_name` | Channel that published the video |
| `watch_date` | Date and time you watched |
| `duration` | Video length (in seconds) |
| `category` | Video category |
| `view_count` | Total views on the video |
| `like_count` | Total likes |

## Configuration

### Getting Your YouTube Data

1. Go to [Google Takeout](https://takeout.google.com/)
2. Deselect all products except **YouTube and YouTube Music**
3. Click "All YouTube data included" → Select only **history**
4. Choose export format (JSON recommended)
5. Download and extract `watch-history.json`

### Obtaining YouTube API Key

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable **YouTube Data API v3**
4. Navigate to Credentials → Create Credentials → API Key
5. Copy the key to your `.env` file

### API Quota Management

The YouTube Data API has daily quota limits (10,000 units/day by default). This tool implements:
- Batch processing to minimize API calls
- Automatic retry logic for rate limiting
- Progress tracking for large datasets

## Power BI Integration

1. Open Power BI Desktop
2. Get Data → Excel → Select generated `youtube_analysis.xlsx`
3. Load the data into Power BI
4. Create visualizations for:
   - Watch time trends over time
   - Top channels by views
   - Content category breakdown
   - Daily/weekly viewing patterns
   - Average video duration preferences


### Project Structure

```
youtube-watch-history-analyzer/
├── main.py                 # Main execution script
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── config.py              # Configuration settings
├── src/
│   ├── parser.py          # Watch history parser
│   ├── api_client.py      # YouTube API client
│   ├── data_processor.py  # Data transformation
│   └── exporter.py        # Excel export handler
├── output/                # Generated files
└── README.md
```
## Contact

Have questions or suggestions? Feel free to:
- Open an issue on GitHub
- Submit a pull request
- Reach out via LinkedIn (https://www.linkedin.com/in/hasan-shinnar/)

</div>

=======
![Image](https://github.com/user-attachments/assets/3883f127-030c-4f78-b829-b564f79458fb)
![Image](https://github.com/user-attachments/assets/18db6ab8-dfaa-495c-8931-87bc2a506da8)
>>>>>>> parent of 2872a3d (Update README.md)
