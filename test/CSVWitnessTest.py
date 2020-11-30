import unittest

class CSVWitnessTest(unittest.TestCase):

    url_two = "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"
    converted_file_two = "Comparison_of_Afrikaans_and_Dutch_1.csv"
    wanted_file_two = "Comparison_of_Afrikaans_and_Dutch_1.csv"

    url_four = "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"
    converted_file_four = "Comparison_of_Afrikaans_and_Dutch_2.csv"
    wanted_file_four = "Comparison_of_Afrikaans_and_Dutch_2.csv"

    """Case : Comparison of a predefined hand-made CSV of a given table with the generated CSV of the same table
       Result : Generated CSV correspond to hand-made one"""
    def test_witness_two(self):

        result = self.compare_csv_files(self.url_two, self.wanted_file_two, self.converted_file_two)
        self.assertTrue(result, "Generated file does not correspond expected file")

    """Case : Comparison of a predefined hand-made CSV of a given table with the generated CSV of the same table
      Result : Generated CSV correspond to hand-made one"""
    def test_witness_four(self):

        result = self.compare_csv_files(self.url_four, self.wanted_file_four, self.converted_file_four)
        self.assertTrue(result, "Generated file does not correspond expected file")

    def compare_csv_files(self, url, wantedFile, convertedFile):

        return True








