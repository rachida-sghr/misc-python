quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

import random 
import json

def read_characters_from_file(characters_file):
    values = []
    with open(characters_file, "r") as f:
        data = json.load(f)
        for character in data.values():
            values.append(character)
    return values

def get_random_item(lst):
  return lst[random.randint(0, len(lst) - 1)]

def capitalize(words):
    for word in words:
        word.capitalize()


def message(quote,character):
    c_quote = quote.capitalize()
    c_character = character.capitalize()
    return "\"{}\", a dit {}" .format(c_character,c_quote)

user_answer = input ('Tapez entrée pour connître une autre citation ou B pour quitter le programme')

while user_answer != "B":
    print(message(get_random_item(characters),get_random_item(quotes)))
    user_answer = input ('Tapez entrée pour connître une autre citation ou B pour quitter le programme')
