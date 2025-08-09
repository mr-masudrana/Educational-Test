import requests

# তোমার data.json এর লিঙ্ক
DATA_URL = "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/script_api/data.json"

try:
    # JSON ডাউনলোড
    response = requests.get(DATA_URL)
    response.raise_for_status()
    channels = response.json()
except Exception as e:
    print("❌ JSON ডাউনলোডে সমস্যা:", e)
    exit()

# M3U কন্টেন্ট শুরু
m3u_content = "#EXTM3U\n\n"

for ch in channels:
    # হেডার লিস্ট তৈরি
    headers = []
    if ch.get("cookie"):
        headers.append(f"Cookie={ch['cookie']}")
    if ch.get("user_agent"):
        headers.append(f"User-Agent={ch['user_agent']}")

    header_str = "|" + "|".join(headers) if headers else ""

    # চ্যানেল তথ্য যোগ
    m3u_content += (
        f'#EXTINF:-1 tvg-name="{ch["name"]}" tvg-logo="{ch["logo"]}" '
        f'group-title="{ch["category_name"]}",{ch["name"]}\n'
        f'{ch["link"]}{header_str}\n\n'
    )

# playlist.m3u ফাইলে লেখা
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)

print("✅ playlist.m3u তৈরি হয়েছে!")
