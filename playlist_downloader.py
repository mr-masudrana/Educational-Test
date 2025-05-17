import requests
import re

# Step 1: Access Toffee homepage to get new cookies
url = "https://toffeelive.com"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

session = requests.Session()
resp = session.get(url, headers=headers)

# Step 2: Try to extract Edge-Cache-Cookie (from set-cookie or session cookies)
cookies = session.cookies.get_dict()
edge_cookie = cookies.get("Edge-Cache-Cookie", None)

if edge_cookie:
    print("Edge-Cache-Cookie found:", edge_cookie)

    # Step 3: Use the cookie in further requests
    m3u8_url = "https://bldcmprod-cdn.toffeelive.com/cdn/live/sports_highlights/playlist.m3u8"
    headers = {
        "Origin": "https://bldcmprod-cdn.toffeelive.com",
        "User-Agent": "Toffee (Linux;Android 14) AndroidXMedia3/1.1.1",
        "Cookie": f"Edge-Cache-Cookie={edge_cookie}",
        "Referer": "https://toffeelive.com",
    }

    response = requests.get(m3u8_url, headers=headers)
    if response.status_code == 200:
        with open("playlist.m3u8", "w") as f:
            f.write(response.text)
        print("Playlist downloaded.")
    else:
        print("Failed to download playlist:", response.status_code)
else:
    print("Could not find Edge-Cache-Cookie.")
