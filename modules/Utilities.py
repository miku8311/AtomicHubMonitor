import sys
import json
import os

class Utilities(): 

    def __init__(self):
        pass

    @staticmethod
    def save_json_file(json_file, data_struc): 
        """Saves Json data to disk file""" 

        with open(json_file, 'w') as file: 
            data = json.dump(data_struc, file)

    @staticmethod
    def load_json_file(json_file): 
        """Loads a Json file from disk"""

        try: 
            with open(json_file, 'r') as file: 
                data_struct = json.load(file)

            return data_struct

        except Exception: 
            return None

    @staticmethod 
    def loads_json(response_text): 
        """Encapsulates json library loads method"""

        return json.loads(response_text);

