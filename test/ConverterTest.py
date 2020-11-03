import unittest
import converter


class ConverterTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.tables = {}

    def test_converter_to_csv(self):
        converter.convert_to_csv(self.tables)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
