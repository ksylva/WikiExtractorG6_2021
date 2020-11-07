import unittest
import htmlTablesExtractor as extractor

class HtmlTablesExtractorTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.urls = extractor.get_urls()
        self.tables = extractor.get_html_tables(**self.urls)

    def test_urls(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
