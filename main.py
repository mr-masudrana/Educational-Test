import requests
import json

# যেসব চ্যানেল লিংক চেক করে কুকি আপডেট করতে হবে
channel_links = [
    "https://bldcmprod-cdn.toffeelive.com/cdn/live/sports_highlights/playlist.m3u8",
    "https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_movie/playlist.m3u8",
    "https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_drama/playlist.m3u8"
]

headers = {
    "User-Agent": "Toffee (Linux;Android 14) AndroidXMedia3/1.1.1/64103898/4d2ec9b8c7534adc"
}

def get_cookie(url):
    try:
        response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
        cookie = response.headers.get("Set-Cookie", "")
        return cookie.strip()
    except Exception as e:
        print(f"Failed to fetch cookie from {url}: {e}")
        return ""

# আগের ফাইল লোড
with open("toffee_playlist.m3u", "r", encoding="utf-8") as f:
    playlist = json.load(f)

# প্রতিটি লিংক থেকে কুকি নিয়ে আপডেট করা
for channel in playlist:
    link = channel.get("link")
    if link in channel_links:
        new_cookie = get_cookie(link)
        if new_cookie:
            channel["cookie"] = new_cookie
            print(f"Updated cookie for {channel['name']}")
        else:
            print(f"No cookie fetched for {channel['name']}")

# আবার ফাইলে সেভ করা
with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
    json.dump(playlist, f, indent=2)

print("Playlist updated successfully.")
