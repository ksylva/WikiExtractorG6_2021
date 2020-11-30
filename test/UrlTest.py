import unittest
import htmlTablesExtractor as ht
from htmlTablesExtractor import get_urls as url


class MyTestCase(unittest.TestCase):
    url_prefix = "https://en.wikipedia.org/wiki/"


    def test_something(self):
        self.assertEqual(True, False)


    def test_url_prefix_valid(self):
        for url_key, url_value in url().items():
            prefix_pos = url_value.rindex("/")
            prefix = url_value[:prefix_pos + 1]

            self.assertEqual(prefix, self.url_prefix)



if __name__ == '__main__':
    unittest.main()
