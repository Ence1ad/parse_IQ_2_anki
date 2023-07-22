from anki.create_pkg import create_anki_package
from json_io.json_io import save_json, get_json
from parser.get_html import get_html_file
from parser.parse_data import interview_question_parser


def main(path_to_file):
    data = interview_question_parser(path_to_file)
    # Get title from dict
    title = list(data.keys())[0]
    save_json(title, data)
    json_data = get_json(title)
    create_anki_package(data=json_data, package_name=title)


if __name__ == '__main__':
    resource_slug = 'selenium-interview-questions'
    html_file_path = get_html_file(resource_slug)
    if html_file_path:
        main(html_file_path)
    else:
        print("Please write correct slug")
