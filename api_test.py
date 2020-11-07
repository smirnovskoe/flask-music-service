
import requests
import unittest


class MusicApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:9996/api"
    MUSIC_URL = f"{API_URL}/music"
    NEW_TRACK = {
        "singer": "Abba",
        "song": "Happy New Year"
    }

    def test_1_get_all_tracks(self):
        """GET request to /api/music returns the details of all books"""
        r = requests.get(MusicApiTest.MUSIC_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()['tracks']), 4)

    def test_2_add_new_track(self):
        """POST request to /api/music to create a new track"""
        r = requests.post(MusicApiTest.MUSIC_URL, json=MusicApiTest.NEW_TRACK)
        self.assertEqual(r.status_code, 201)

    def test_3_get_new_track(self):
        id = 5
        r = requests.get(f"{MusicApiTest.MUSIC_URL}/{id}")
        self.assertEqual()
