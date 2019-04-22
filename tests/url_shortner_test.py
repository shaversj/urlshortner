import unittest
import json

from program import app

# set our application to testing mode
app.testing = True


class URLShortnerTest(unittest.TestCase):
    def test_post_URL(self):
        with app.test_client() as client:
            message = {"url": "http://www.google.com"}
            response = client.post("/postURL", json=message)

            # self.assertTrue(response.is_json)
            # print(response.get_json())
            self.assertEqual(response.data, b'{"url": "http://www.google.com"}')


if __name__ == "__main__":
    unittest.main()
