from pathlib import Path
from requests import Response

from util.router import path_to_html


def get_path_html_file(title: str, dirname: str | None = None) -> str:
    path = path_to_html
    if dirname:
        path_to_file = f'{path}/{dirname}/{title}'
    else:
        path_to_file = f'{path}/{title}'
    if Path.exists(Path(path).joinpath(title)):
        return path_to_file


def save_html_data(dirname: str, title: str, response: Response):
    path = path_to_html
    path_to_file = f'{path}/{dirname}/{title}'
    with open(file=path_to_file, mode='w', encoding='utf-8') as f:
        f.write(response.text)
    return path_to_file
