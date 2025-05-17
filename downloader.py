import requests

ts_url = "https://bldcmprod-cdn.toffeelive.com/live/sony_max_hd_576/1747446724614.ts"
ts_filename = ts_url.split("/")[-1]

# Download .ts segment
print(f"Downloading {ts_filename}...")
response = requests.get(ts_url)
with open(ts_filename, "wb") as f:
    f.write(response.content)
print("Download completed.")

# Save playlist
m3u8_content = """#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0

#EXTINF:10.0,
{}

#EXT-X-ENDLIST
""".format(ts_filename)

with open("playlist.m3u8", "w") as f:
    f.write(m3u8_content)

print("playlist.m3u8 created.")
