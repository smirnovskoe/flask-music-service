
import requests
import unittest


class FlaskApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:9997/api"
    MUSIC_URL = f"{API_URL}/music"

    def test_1_get_all_tracks(self):
        r = requests.get(FlaskApiTest.MUSIC_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json), 4)
