import requests
import json

PRIMARY_URL = "https://raw.githubusercontent.com/byte-capsule/Toffee-Channels-Link-Headers/main/toffee_channel_data.json"
BACKUP_URL = "https://cdn.jsdelivr.net/gh/byte-capsule/Toffee-Channels-Link-Headers@main/toffee_channel_data.json"

def fetch_channel_data():
    try:
        print("Trying primary source...")
        r = requests.get(PRIMARY_URL, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Primary failed: {e}, trying backup...")
        r = requests.get(BACKUP_URL)
        r.raise_for_status()
        return r.json()

def generate_m3u(channels):
    output = "#EXTM3U\n"
    for ch in channels:
        output += f'#EXTINF:-1 tvg-logo="{ch["logo"]}",{ch["name"]}\n'
        output += f'#EXTVLCOPT:http-referrer={ch["referrer"]}\n'
        output += f'#EXTVLCOPT:http-user-agent={ch["userAgent"]}\n'
        output += f'#EXTVLCOPT:http-cookie={ch["cookie"]}\n'
        output += f'{ch["link"]}\n\n'
    return output

def save_m3u(content):
    with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    try:
        channels = fetch_channel_data()
        m3u_content = generate_m3u(channels)
        save_m3u(m3u_content)
        print("Playlist updated successfully.")
    except Exception as e:
        print(f"Failed to update: {e}")
