import sys
import json
import os

class Utilities(): 

    def __init__(self):
        pass

    @staticmethod
    def SaveJson(json_file, data_struc): 
        """ """ 

        with open(json_file, 'w') as file: 
            data = json.dump(data_struc, file)

    @staticmethod
    def LoadJson(json_file): 
        """ """

        try: 
            with open(json_file, 'r') as file: 
                data_struct = json.load(file)

            return data_struct

        except Exception: 
            return None
