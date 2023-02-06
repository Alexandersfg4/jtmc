from typing import List, Dict, Union
import json


class Converter:
    def __init__(self, data: str):
        self.data = data
        self.models = dict()

    def to_model(self) -> dict:
        dict_data = self.__to_dict(self.data)
        self.__convert_dict(dict_data)
        return self.models

    def __convert_dict(self, data: Union[List, Dict], default_model: str = "ROOT"):
        if isinstance(data, dict):
            self.models[default_model] = set()
            for key in data.keys():
                self.models.get(default_model).add(self.__to_snake_case(key))
            for key, value in data.items():
                if isinstance(data[key], dict):
                    default_model = key.upper()
                    self.__convert_dict(value, default_model)
                elif isinstance(data[key], list):
                    default_model = key.upper().strip('S')
                    self.__convert_dict(value, default_model)
        elif isinstance(data, list):
            for item in data:
                self.__convert_dict(item, default_model)

    @staticmethod
    def __to_dict(data):
        return json.loads(data)

    @staticmethod
    def __to_snake_case(key_name: str):
        converted_key = ""
        for i, letter in enumerate(key_name):
            if letter.isupper() and i == 0:
                converted_key += letter.lower()
            elif letter.isupper():
                converted_key += f"_{letter.lower()}"
            else:
                converted_key += letter
        return converted_key






