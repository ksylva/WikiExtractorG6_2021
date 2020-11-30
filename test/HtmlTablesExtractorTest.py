import unittest
import htmlTablesExtractor as extractor


class HtmlTablesExtractorTest(unittest.TestCase):
    #def __init__(self):
        #super().__init__()
        #self.urls = extractor.get_urls()
        #self.tables = extractor.get_html_tables(**self.urls)

    #def test_urls(self):
        #self.assertEqual(True, False)

    def test_get_number_of_tables_per_page(self):
        urls = {"Comparison_of_Afrikaans_and_Dutch":"https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"}
        nb_tables = extractor.get_number_of_tables_per_page(**urls)
        self.assertEqual({"Comparison_of_Afrikaans_and_Dutch":3},nb_tables,"Generated tables does not correspond expected tables")

        #url = ["https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"]
        #value_list = [val for (k, val) in urls.items() if nb_tables == 4]
        #self.assertIsNot(val,extractor.__url_state(url))
        #self.assertRaises(ValueError,extractor.get_number_of_tables_per_page(**urls),4)

if __name__ == '__main__':
    unittest.main()
