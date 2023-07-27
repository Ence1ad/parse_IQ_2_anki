from anki.create_pkg import create_anki_package
from json_io.json_io import save_json, get_json
from parser.get_html import save_html
from parser.parse_learnshell_data import get_slug_list, get_content


def main(path_to_file: str) -> None:
    slug_list = get_slug_list(path_to_file)
    dirname = title = path_to_file.split('/')[-1].split('.')[-2]
    cards = []
    for slug in slug_list:
        path_to_content = save_html(dirname, slug)
        data = get_content(path_to_content)
        cards.append(data)
    data = {f'{title}': cards}
    save_json(title, data)
    json_data = get_json(title)
    create_anki_package(data=json_data, package_name=title)


if __name__ == '__main__':
    path_to_index = save_html()
    if path_to_index:
        main(path_to_index)
    else:
        print("Please write correct slug")
