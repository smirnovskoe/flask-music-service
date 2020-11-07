
import requests
import unittest


class MusicApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:9995/api"
    MUSIC_URL = f"{API_URL}/music"
    NEW_TRACK = {
        "singer": "Abba",
        "song": "Happy New Year"
    }

    START_ID = 4

    def test_1_get_all_tracks(self):
        """GET request to /api/music returns the details of all books"""
        r = requests.get(MusicApiTest.MUSIC_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()['tracks']), MusicApiTest.START_ID)

    def test_2_add_new_track(self):
        """POST request to /api/music to create a new track"""
        r = requests.post(MusicApiTest.MUSIC_URL, json=MusicApiTest.NEW_TRACK)
        self.assertEqual(r.status_code, 201)

    def test_3_get_new_track(self):
        id = 5
        r = requests.get(f"{MusicApiTest.MUSIC_URL}/{id}")
        self.assertEqual(r.status_code, 200)
        new_track = MusicApiTest.NEW_TRACK
        new_track['id'] = id
        self.assertDictEqual(r.json()['track'][0], new_track)

    def test_4_update_existing_book(self):
        id = 1
        new_track = {
            'singer': 'Moses',
            'song': 'A Million On My Soul'
        }
        r = requests.put(f"{MusicApiTest.MUSIC_URL}/{id}", json=new_track)
        self.assertEqual(r.status_code, 200)

    def test_5_get_new_track_after_update(self):
        id = 1
        new_track = {
            'singer': 'Moses',
            'song': 'A Million On My Soul'
        }
        r = requests.get(f"{MusicApiTest.MUSIC_URL}/{id}")
        new_track['id'] = id
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json()['track'], new_track)
