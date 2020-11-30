import unittest
from htmlTablesExtractor import get_urls as url
import htmlTablesExtractor as extractor


class UrlTest(unittest.TestCase):

    url_prefix = "https://en.wikipedia.org/wiki/"

    #Test on valid url

    def test_urlValid(self):
        urls = extractor.get_urls()
        for url_key, url_value in urls.items():
            status_code = extractor.url_state(url_value)
            self.assertEqual(status_code, True)

    # Test on url different from empty strings

    def test_urlNull(self):
        urls = extractor.get_urls()
        for url_key, url_value in urls.items():
            self.assertNotEqual(url_value, '')

    # def test_urlInvalid(self):
    #     urls = extractor.get_urls()
    #     for url_key, url_value in urls.items():
    #         status_code = extractor.url_state(url_value)
    #
    #             self.assertEqual(status_code, False)
    #

    def test_url_prefix_valid(self):
        for url_key, url_value in url().items():
            prefix_pos = url_value.rindex("/")
            prefix = url_value[:prefix_pos + 1]

            self.assertEqual(prefix, self.url_prefix)


if __name__ == '__main__':
    unittest.main()
