import json

from util.router import path_to_json


def save_json(filename: str, data: dict) -> None:
    title = filename + '.json'
    file = f'{path_to_json}/{title}'
    with open(file=file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_json(filename: str) -> json:
    title = filename + '.json'
    file = f'{path_to_json}/{title}'
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        return data

