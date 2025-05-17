import requests

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

headers = {
    "User-Agent": "Toffee (Linux;Android 14) AndroidXMedia3/1.1.1/64103898/4d2ec9b8c7534adc",
    "Origin": "https://toffeelive.com",
    "Referer": "https://toffeelive.com/",
    "Accept": "*/*"
}

m3u_data = "#EXTM3U\n"

for ch in channels:
    print(f"[*] Processing: {ch['name']}")
    try:
        r = requests.get(ch["link"], headers=headers)
        cookie_header = r.headers.get("set-cookie", "")
        edge_cookie = ""

        for c in cookie_header.split(";"):
            if "Edge-Cache-Cookie" in c:
                edge_cookie = c.strip()
                break

        if not edge_cookie:
            print(f"[!] Edge-Cache-Cookie not found for {ch['name']}, skipping.")
            continue

        m3u_data += f'#EXTINF:-1 tvg-id="{ch["name"]}" tvg-logo="{ch["logo"]}",{ch["name"]}\n'
        m3u_data += f'#EXTVLCOPT:http-referrer=https://toffeelive.com/\n'
        m3u_data += f'#EXTVLCOPT:http-user-agent={headers["User-Agent"]}\n'
        m3u_data += f'#EXTVLCOPT:http-cookie={edge_cookie}\n'
        m3u_data += f'{ch["link"]}\n\n'

    except Exception as e:
        print(f"[!] Error for {ch['name']}: {e}")

with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_data)

print("[✓] toffee_playlist.m3u created successfully.")
