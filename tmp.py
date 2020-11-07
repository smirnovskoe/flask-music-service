import requests

NEW_TRACK = {
        "singer": "Abba",
        "song": "Happy New Year"
    }

id = 5

new_track = NEW_TRACK
new_track['id'] = 5

r = requests.get("http://127.0.0.1:9995/api/music/5")

print(r.status_code)
print(new_track)
print(r.json()['track'][0])
