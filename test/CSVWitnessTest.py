import unittest


class CSVWitnessTest(unittest.TestCase):
    url_two = "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"
    converted_file_two = "Comparison_of_Afrikaans_and_Dutch_3.csv"
    wanted_file_two = "Comparison_of_Afrikaans_and_Dutch_3.csv"

    wanted_file_three = ""
    converted_file_three = ""

    ground_truth_path = "../groundTruth/"
    extracted_path = "../output/"

    url_four = "https://en.wikipedia.org/wiki/Comparison_of_Afrikaans_and_Dutch"
    converted_file_four = "Comparison_of_Afrikaans_and_Dutch_2.csv"
    wanted_file_four = "Comparison_of_Afrikaans_and_Dutch_2.csv"

    """Case : Comparison of a predefined hand-made CSV of a given table with the generated CSV of the same table
       Result : Generated CSV correspond to hand-made one"""

    def test_witness_two(self):
        result = self.compare_csv_files(self.wanted_file_two, self.converted_file_two)
        self.assertTrue(result, "Generated file does not correspond expected file")

    def test_witness_three(self):
        result = self.compare_csv_files(self.wanted_file_three, self.converted_file_three)
        self.assertTrue(result, "Generated file does not correspond expected file")

    """Case : Comparison of a predefined hand-made CSV of a given table with the generated CSV of the same table
      Result : Generated CSV correspond to hand-made one"""

    def test_witness_four(self):
        result = self.compare_csv_files(self.wanted_file_four, self.converted_file_four)
        self.assertTrue(result, "Generated file does not correspond expected file")

    def compare_csv_files(self, wanted_file, converted_file):
        converted = ""
        wanted = ""
        with open(self.extracted_path + converted_file, 'r') as cvt:
            for c_line in cvt:
                converted += c_line
        # print("Converted file is : {}".format(converted))
        with open(self.ground_truth_path + wanted_file, 'r') as wtd:
            for w_line in wtd:
                wanted += w_line
        # print("Wanted file is : {}".format(wanted))
        return converted == wanted
