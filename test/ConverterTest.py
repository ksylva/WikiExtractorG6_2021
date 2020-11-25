# coding=utf-8
import unittest
import converter
import htmlTablesExtractor as extractor


class ConverterTest(unittest.TestCase):
    url1 = "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido"

    # def __init__(self):
    #     super().__init__()
    # self.urls = extractor.get_urls()
    # self.tables = extractor.get_html_tables(**self.urls)

    # def test_converter_to_csv(self):
    #     # converter.convert_to_csv(**self.tables)
    #     self.assertEqual(True, True)

    def test_number_tables(self):
        self.assertEqual(8, extractor.get_number_of_tables_on_page(self.url1), "Number of tables isn't correct")

    def test_check_nb_columns(self):
        urls = {"Comparison_of_Afrikaans_and_Dutch":"https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"}
        table = extractor.get_html_tables(**urls)
        dict = {"Comparison_of_Afrikaans_and_Dutch":table}
        file = converter.convert_to_csv(**dict)

        nbColumnTable = extractor.get_number_of_columns_in_the_table(table)
        nbColumnFile = extractor.get_number_of_columns_in_the_csv(file)

        self.assertEqual(nbColumnTable,nbColumnFile)

    def test_check_nb_rows(self):
        urls = {"Comparison_of_Afrikaans_and_Dutch":"https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"}
        table = extractor.get_html_tables(**urls)
        dict = {"Comparison_of_Afrikaans_and_Dutch":table}
        file = converter.convert_to_csv(**dict)

        nbRowsTable = extractor.get_number_of_rows_in_the_table(table)
        nbRowsFile = extractor.get_number_of_rows_in_the_csv(file)

        self.assertEqual(nbRowsTable,nbRowsFile)



if __name__ == '__main__':
    unittest.main()
