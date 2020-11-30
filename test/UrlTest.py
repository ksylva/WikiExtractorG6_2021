import unittest
import urllib.request as u_req
import htmlTablesExtractor as extractor


class UrlTest(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
