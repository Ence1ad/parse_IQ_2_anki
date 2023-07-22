import random

from genanki import Model
from anki.css.style import style
from anki.templates import front_template, back_template


def get_model():
    # Генерируем model_id один раз и хардкодим в классе Model используем randrange(1 << 30, 1 << 31)
    model_id = random.randrange(1 << 30, 1 << 31)
    my_model = Model(
        model_id,
        'type_1',  # Note type
        fields=[
            {'name': 'Question'},
            {'name': 'Back_Sound'},
            {'name': 'Back_Text'},
            {'name': 'Back_Code'},
            {'name': 'Additional Info'},
            {'name': 'Example'},

        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': front_template,
                'afmt': back_template,
            },
        ], css=style
    )
    return my_model
