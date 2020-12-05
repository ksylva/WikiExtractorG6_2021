import unittest
import htmlTablesExtractor as extractor


class HtmlTablesExtractorTest(unittest.TestCase):
    def test_number_tables(self):
        url1 = "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido"
        self.assertEqual(8, extractor.get_number_of_tables_on_page(url1), "Number of tables isn't correct")

    def test_get_number_of_tables_per_page(self):
        urls = {"Comparison_of_Afrikaans_and_Dutch": "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"}
        nb_tables = extractor.get_number_of_tables_per_page(**urls)
        self.assertEqual({"Comparison_of_Afrikaans_and_Dutch": 3}, nb_tables, "Generated tables does not correspond expected tables")


if __name__ == '__main__':
    unittest.main()
