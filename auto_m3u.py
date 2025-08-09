import requests
import json

# data.json এর লিঙ্ক
DATA_URL = "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/script_api/data.json"

try:
    response = requests.get(DATA_URL)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print("❌ JSON ডাউনলোডে সমস্যা:", e)
    exit()

# ডেটার আসল স্ট্রাকচার দেখা
print("ℹ JSON স্ট্রাকচার:", type(data))
if isinstance(data, dict):
    # যদি dictionary হয়, তাহলে কোন key তে channel list আছে সেটা ঠিক করতে হবে
    if "channels" in data:
        channels = data["channels"]
    elif "data" in data:
        channels = data["data"]
    else:
        print("❌ Channel list খুঁজে পাওয়া যায়নি!")
        exit()
elif isinstance(data, list):
    # যদি সরাসরি list হয়
    channels = data
else:
    print("❌ Unsupported JSON format!")
    exit()

# M3U বানানো
m3u_content = "#EXTM3U\n\n"

for ch in channels:
    if not isinstance(ch, dict):
        continue  # স্ট্রিং বা invalid entry skip করো

    headers = []
    if ch.get("cookie"):
        headers.append(f"Cookie={ch['cookie']}")
    if ch.get("user_agent"):
        headers.append(f"User-Agent={ch['user_agent']}")

    header_str = "|" + "|".join(headers) if headers else ""

    m3u_content += (
        f'#EXTINF:-1 tvg-name="{ch["name"]}" tvg-logo="{ch["logo"]}" '
        f'group-title="{ch["category_name"]}",{ch["name"]}\n'
        f'{ch["link"]}{header_str}\n\n'
    )

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)

print("✅ playlist.m3u তৈরি হয়েছে!")
