import datetime

playlist = [
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

with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for channel in playlist:
        f.write(f'#EXTINF:-1 tvg-logo="{channel["logo"]}",{channel["name"]}\n')
        f.write(f'{channel["link"]}\n')

print("Playlist updated:", datetime.datetime.now())
