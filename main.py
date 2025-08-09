import requests
import json

# Toffee চ্যানেল ডেটার URL
json_url = "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/script_api/data.json"

try:
    # JSON ডেটা সংগ্রহ
    response = requests.get(json_url, timeout=10)
    response.raise_for_status()
    data = response.json()

    # চ্যানেল তথ্য সংগ্রহ
    channels = data.get("channels", [])

    # নতুন প্লেলিস্ট তৈরি
    playlist = []
    for channel in channels:
        name = channel.get("name", "")
        link = channel.get("link", "")
        logo = channel.get("logo", "")
        headers = channel.get("headers", {})
        cookie = headers.get("cookie", "")

        playlist.append({
            "name": name,
            "link": link,
            "logo": logo,
            "origin": "https://bldcmprod-cdn.toffeelive.com",
            "referrer": "",
            "userAgent": "Toffee (Linux;Android 14) AndroidXMedia3/1.1.1/64103898/4d2ec9b8c7534adc",
            "cookie": cookie,
            "drmScheme": "",
            "drmLicense": ""
        })

    # প্লেলিস্ট ফাইল সংরক্ষণ
    with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
        json.dump(playlist, f, indent=2)

    print("✅ toffee_playlist.m3u ফাইল সফলভাবে তৈরি হয়েছে।")

except requests.RequestException as e:
    print(f"❌ ডেটা সংগ্রহে সমস্যা: {e}")
except json.JSONDecodeError as e:
    print(f"❌ JSON ডেটা পার্স করতে সমস্যা: {e}")
except Exception as e:
    print(f"❌ একটি অপ্রত্যাশিত ত্রুটি ঘটেছে: {e}")
