import requests
import json

URL = "https://toffeelive.com/api/v1/programs/live"  # উদাহরণ URL
COOKIE_FILE = "cookie.txt"
PLAYLIST_FILE = "toffee_playlist.m3u"

def fetch_cookie():
    # নতুন Cookie পাওয়ার জন্য API বা HEAD Request (Demo only)
    response = requests.head("https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_movie/playlist.m3u8")
    cookie = response.headers.get('Set-Cookie', '')
    if "Edge-Cache-Cookie=" in cookie:
        return cookie.split("Edge-Cache-Cookie=")[1].split(";")[0]
    return ""

def generate_playlist(cookie):
    channels = [
        {
            "name": "TOFFEE Movies VIP",
            "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_movie/playlist.m3u8"
        },
        {
            "name": "TOFFEE Sports VIP",
            "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/sports_highlights/playlist.m3u8"
        }
    ]

    lines = ["#EXTM3U"]
    for ch in channels:
        lines.append(f'#EXTINF:-1,{ch["name"]}')
        lines.append(f'{ch["link"]}|Cookie=Edge-Cache-Cookie={cookie}')
    
    with open(PLAYLIST_FILE, "w") as f:
        f.write("\n".join(lines))

def main():
    cookie = fetch_cookie()
    with open(COOKIE_FILE, "w") as f:
        f.write(cookie)
    generate_playlist(cookie)

if __name__ == "__main__":
    main()
