import requests
import datetime

# Toffee চ্যানেলগুলোর তথ্য
channels = [
    {
        "name": "TOFFEE Sports VIP",
        "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/sports_highlights/playlist.m3u8",
        "logo": "https://images.toffeelive.com/images/program/19779/logo/240x240/mobile_logo_975410001725875598.png"
    },
    {
        "name": "TOFFEE Movies VIP",
        "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_movie/playlist.m3u8",
        "logo": "https://images.toffeelive.com/images/program/2708/logo/240x240/mobile_logo_724353001725875591.png"
    },
    {
        "name": "TOFFEE Dramas VIP",
        "link": "https://bldcmprod-cdn.toffeelive.com/cdn/live/toffee_drama/playlist.m3u8",
        "logo": "https://images.toffeelive.com/images/program/44878/logo/240x240/mobile_logo_764950001725875605.png"
    }
]

# Cookie সংগ্রহের ফাংশন
def get_cookie():
    headers = {
        "User-Agent": "Toffee (Linux;Android 14) AndroidXMedia3/1.1.1",
    }
    response = requests.get("https://toffeelive.com", headers=headers)
    cookie = response.headers.get("Set-Cookie", "")
    if cookie:
        cookie_value = cookie.split(';')[0]
        return cookie_value
    return ""

# Cookie সংগ্রহ
cookie = get_cookie()

# .m3u ফাইল তৈরি
with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for channel in channels:
        f.write(f'#EXTINF:-1 tvg-logo="{channel["logo"]}",{channel["name"]}\n')
        if cookie:
            f.write(f'#EXTVLCOPT:http-header=Cookie={cookie}\n')
        f.write(f'{channel["link"]}\n')

print("Playlist updated at", datetime.datetime.now())
