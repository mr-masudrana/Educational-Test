import requests
from datetime import datetime
import json

# টার্গেট লাইভ চ্যানেল URL (যেটি .m3u8 ফর্মে থাকে)
url = "https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_movie/playlist.m3u8"

headers = {
    "User-Agent": "Toffee (Linux;Android 14) AndroidXMedia3/1.1.1/64103898/4d2ec9b8c7534adc",
    "Origin": "https://toffeelive.com",
    "Referer": "https://toffeelive.com/",
    "Accept": "*/*"
}

print("[*] Requesting playlist...")
response = requests.get(url, headers=headers)

# Cookie ধরার চেষ্টা
cookie = response.headers.get("set-cookie") or response.request.headers.get("cookie")

if not cookie:
    print("[!] Cookie not found!")
    exit(1)

# Cookie থেকে শুধুমাত্র Edge-Cache-Cookie আলাদা করি
edge_cookie = None
for c in cookie.split(";"):
    if "Edge-Cache-Cookie" in c:
        edge_cookie = c.strip()
        break

if not edge_cookie:
    print("[!] Edge-Cache-Cookie not found.")
    exit(1)

# নতুন m3u ফাইল তৈরি
playlist = f"""#EXTM3U
#EXTINF:-1 tvg-id="TOFFEE" tvg-logo="https://images.toffeelive.com/images/program/2708/logo/240x240/mobile_logo_724353001725875591.png",TOFFEE Movie VIP
#EXTVLCOPT:http-referrer=https://toffeelive.com/
#EXTVLCOPT:http-user-agent=Toffee (Linux;Android 14)
#EXTVLCOPT:http-cookie={edge_cookie}
{url}
"""

with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist)

print("[✓] toffee_playlist.m3u created successfully.")
