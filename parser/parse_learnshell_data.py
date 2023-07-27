from bs4 import BeautifulSoup


def get_slug_list(path_to_file):
    with open(file=path_to_file, mode='r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, "html.parser")
        content = soup.find('div', {"id": "inner-text"})
        a_list = content.find_all('a')
        lst = []
        for a in a_list:
            lst.append(a['href'])
        return lst


def get_content(path_to_file: str) -> dict:
    card = {"Question": None, "Back_Text": None}
    with open(file=path_to_file, mode='r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, "html.parser")
        content = soup.find('div', {"id": "inner-text"})
        title = path_to_file.split('/')[-1].split('.')[-2]
        card["Question"] = title
        card["Back_Text"] = content
        card_data = {"Question": f'{card["Question"]}',
                     "Back_Text": f'{card["Back_Text"]}'}
        return card_data
