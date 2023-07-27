import requests
from requests import Response

from util.router import BASE_URL
from util.html_io import get_path_html_file, save_html_data


def save_html(dirname: str | None = None, slug: str | None = None) -> str:
    if slug:
        url = BASE_URL + slug
        title = url.split('/')[-1] + '.html'
    else:
        url = BASE_URL
        title = url.split('.')[-2] + '.html'
    path_to_html = get_path_html_file(title, dirname=dirname)
    if path_to_html:
        return path_to_html
    else:
        r: Response = requests.get(url)
        if r.status_code == 200:
            return save_html_data(dirname, title, r)
