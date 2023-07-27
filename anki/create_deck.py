import random

import genanki

from anki.model import get_model


def create_deck(*, data, deck_name):
    """Функция создает колоду используя данные, необходимую html разметку необходимо указывать вручную"""
    # Генерируем model_id один раз и хардкодим в классе Deck используем randrange(1 << 30, 1 << 31)
    deck_id = random.randrange(1 << 30, 1 << 31)
    deck = genanki.Deck(deck_id, deck_name)
    my_model = get_model()
    for dd in data[deck_name]:
        note = genanki.Note(model=my_model, fields=[dd['Question'], '', dd['Back_Text'], '', '', ''])
        deck.add_note(note)
    return deck
