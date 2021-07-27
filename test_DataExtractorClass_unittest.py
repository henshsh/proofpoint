import sys
import unittest
from DataExtractorClass import DataExtractor
import json
import pathlib
import os


class TestDataExtractorClass(unittest.TestCase):

    # Checking a case of a valid json and its supposed to be output
    def test_correct_json(self):
        my_test_obj = DataExtractor(pathlib.Path(os.path.join(sys.path[0], 'json_test_input')))
        my_test_obj.process_data()
        my_test_obj.save_data()
        with open(os.path.join(sys.path[0], 'json_test_input_new'), 'r') as my_output:
            output_content = my_output.read()
        with open(os.path.join(sys.path[0], 'json_test_output'), 'r') as my_example_output:
            example_output_content = my_example_output.read()

        self.assertEqual(output_content, example_output_content, 'should be True')

    # Checking a case of an invalid json
    def test_incorrect_json(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            my_test_obj = DataExtractor(pathlib.Path(os.path.join(sys.path[0], 'invalid_json')))


if __name__ == '__main__':
    unittest.main()
