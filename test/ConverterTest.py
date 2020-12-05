# coding=utf-8
import unittest
import converter
import htmlTablesExtractor as extractor


class ConverterTest(unittest.TestCase):

    # def __init__(self):
    #     super().__init__()
    # self.urls = extractor.get_urls()
    # self.tables = extractor.get_html_tables(**self.urls)

    # def test_converter_to_csv(self):
    #     # converter.convert_to_csv(**self.tables)
    #     self.assertEqual(True, True)

    def test_check_nb_columns(self):
        urls = {"Comparison_of_Afrikaans_and_Dutch":"https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"}
        table = extractor.get_html_tables(**urls)
        dict = {"Comparison_of_Afrikaans_and_Dutch":table}
        file = converter.convert_to_csv(**dict)

        nbColumnTable = extractor.get_number_of_columns_in_the_table(table)
        nbColumnFile = extractor.get_number_of_columns_in_the_csv(file)

        self.assertEqual(nbColumnTable,nbColumnFile)

    def test_check_nb_rows(self):
        url = "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"
        table_num = 0
        csv_file = "Comparison_of_Afrikaans_and_Dutch_1.csv"

        nbRowsTable = extractor.get_number_of_rows_in_the_table(url, table_num)
        nbRowsFile = get_number_of_rows_in_the_csv(csv_file)

        self.assertEqual(nbRowsTable, nbRowsFile)


def get_number_of_rows_in_the_csv(converted_file):
    nb_rows = 0
    with open("../output/"+converted_file, 'r') as converted:
        for line in converted:
            nb_rows += 1
    return nb_rows


if __name__ == '__main__':
    unittest.main()
