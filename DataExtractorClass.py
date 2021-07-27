import json
from pathlib import WindowsPath
from datetime import datetime
import re


class DataExtractor:
    def __init__(self, path):
        if isinstance(path, WindowsPath):
            try:
                with open(path, 'r') as my_json_file:
                    self.data = json.load(my_json_file)
                    self.path = str(path)

            except FileNotFoundError:
                print('invalid path')
                raise FileNotFoundError

            except json.decoder.JSONDecodeError as bad_input:
                print('Bad input')
                raise bad_input

        else:
            print('invalid parameter as path')

    # Processing the data that retrieved from the input json
    def process_data(self):
        for key in self.data:
            if isinstance(self.data[key], str):
                # Check if string is in a date convention
                match = re.search(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}', self.data[key])
                if match is not None:
                    try:
                        obj = datetime.strptime(self.data[key], '%Y/%m/%d %H:%M:%S')
                        obj = obj.replace(year=2021)
                        self.data[key] = obj.strftime('%Y/%m/%d %H:%M:%S')

                    # In case of a string in date format but not a valid one as requested in the instructions
                    except ValueError:
                        self.data[key] = self.data[key].replace(' ', '')[::-1]

                # In case of a string that not in a date format
                else:
                    self.data[key] = self.data[key].replace(' ', '')[::-1]

            # In case of a list
            elif isinstance(self.data[key], list):
                self.data[key] = list({}.fromkeys(self.data[key]))

    # Save processed data into a new json with a '_new' extension to the name of the original json
    def save_data(self):
        with open(self.path + '_new', 'w') as new_json_file:
            json.dump(self.data, new_json_file)
