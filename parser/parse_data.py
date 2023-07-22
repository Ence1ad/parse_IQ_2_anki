from bs4 import BeautifulSoup


def interview_question_parser(path_to_file):
    with open(file=path_to_file, mode='r') as f:
        card = {"Question": None, "Back_Text": None, "Additional Info": None}
        cards = []
        soup = BeautifulSoup(f, "html.parser")

        article = soup.find('article',
                            {"class": "post-full post no-image page no-image column is-marginless is-paddingless"})
        title = article.find('h1').get_text()

        content = article.find('div', {"class": "sub-section-container"})
        questions_list = _get_questions_list(soup)
        for question, answer in zip(content.find_all('h4'), content.find_all('div', {"class": "answer"})):
            card["Question"] = question.get_text()
            card["Back_Text"] = answer
            for item in questions_list:
                if item['question'] == card["Question"]:
                    card["Additional Info"] = item['title']
            card_data = {"Question": f'{card["Question"]}',
                         "Back_Text": f'{card["Back_Text"]}',
                         "Additional Info": card["Additional Info"]
                         }

            cards.append(card_data)
    data = {f'{title}': cards}
    return data


def _get_questions_list(soup: BeautifulSoup) -> list[dict[str: str]]:
    question_container = soup.find('div', {"class": "questions-container"})
    questions = question_container.find_all('div', {"class": "is-size-6"})
    lst_of_question = []
    dd = {}
    for cat in questions:
        dd["title"] = cat.find('a').get_text()
        for question in cat.find_all('li'):
            dd["question"] = question.find('a').get_text()
            lst_of_question.append({"title": dd["title"], "question": dd["question"]})
    return lst_of_question
