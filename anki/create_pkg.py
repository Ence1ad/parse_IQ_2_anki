import genanki

from anki.create_deck import create_deck
from router import path_to_apkg


def create_anki_package(*, data, package_name='new_package'):
    deck = create_deck(data=data, deck_name=package_name)
    path = path_to_apkg
    # Сохраняет Anki пакет в (*.apkg) файл
    my_package = genanki.Package(deck_or_decks=deck)
    my_package.write_to_file(f'{path}/{package_name}.apkg')
