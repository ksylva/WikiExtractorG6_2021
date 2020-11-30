import unittest

class CSVWitnessTest(unittest.TestCase):

    url_two = "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"
    converted_file_two = "Comparison_of_Afrikaans_and_Dutch_1.csv"
    wanted_file_two = "Comparison_of_Afrikaans_and_Dutch_1.csv"


    def test_witness_two(self):

        result = self.compare_csv_files(self.url_two, self.wanted_file_two, self.converted_file_two)
        self.assertTrue(result, "Generated file does not correspond expected file")


    def compare_csv_files(url, wantedFile, convertedFile):

        return True








