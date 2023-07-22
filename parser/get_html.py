from pathlib import Path

import requests

from router import path_to_html

BASE_URL = 'https://www.adaface.com/blog/'


def get_html_file(slug):
    url = BASE_URL + slug + '/'

    r = requests.get(url)
    if r.url != "https://www.adaface.com":
        title = url.split('/')[-2] + '.html'
        path = path_to_html
        path_to_file = f'{path}/{title}'
        if Path.exists(Path(path).joinpath(title)):
            return path_to_file
        else:
            with open(file=path_to_file, mode='w', encoding='utf-8') as f:
                f.write(r.text)
            return path_to_file
    else:
        return
