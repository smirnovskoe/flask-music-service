import requests

NEW_TRACK = {
        "singer": "Abba",
        "song": "Happy New Year"
    }

r = requests.post("http://127.0.0.1:9996/api/music", json=NEW_TRACK)

print(r.status_code)

#print(len(r.json()['tracks']))