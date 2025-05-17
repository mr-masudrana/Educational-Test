
import requests
import datetime

# Replace this with the actual .m3u8 link (for testing, use a sample open link)
M3U8_URL = "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"

def download_playlist():
    try:
        response = requests.get(M3U8_URL)
        response.raise_for_status()
        with open("playlist.m3u8", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Playlist updated:", datetime.datetime.now())
    except Exception as e:
        print("Error fetching playlist:", e)

if __name__ == "__main__":
    download_playlist()
