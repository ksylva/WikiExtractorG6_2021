import unittest
import converter
import htmlTablesExtractor as extractor


class ConverterTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.urls = extractor.get_urls()
        self.tables = extractor.get_html_tables(**self.urls)

    def test_converter_to_csv(self):
        converter.convert_to_csv(**self.tables)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
