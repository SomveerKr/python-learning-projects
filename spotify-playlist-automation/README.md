# Spotify Playlist Time Machine 🎵

## Description
A Python script that travels back in time! Enter a date, and this tool scrapes the Billboard Hot 100 for that day and automatically creates a private Spotify playlist with those songs.

This project was made during Day 46 of Angela Yu's 100 Days of Python course.

## Features
-   **Web Scraping**: Fetches historical data from Billboard.com.
-   **Spotify Integration**: Uses the Spotify API to search for songs and create playlists.
-   **Error Handling**: Skips songs not found on Spotify automatically.

## Prerequisites
-   Python 3.x
-   Spotify Account
-   Spotify Developer App (for Client ID & Secret)

## Installation
1.  Clone the repository or download the files.
2.  Install dependencies:
    ```bash
    pip install requests beautifulsoup4 spotipy python-dotenv
    ```
3.  Create a `.env` file in the project directory with your Spotify credentials:
    ```env
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    ```

## Usage
1.  Run the script:
    ```bash
    python main.py
    ```
2.  Enter the date you want to travel to (format: `YYYY-MM-DD`).
3.  Check your Spotify account for the new playlist!
