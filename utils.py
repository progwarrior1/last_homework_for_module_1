import random

import requests

from basicclass import Bassic_word
#
# import json


import json

def load_questions():
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def load_random_file(word):
    word2 = []
    for name in word:
        word2 = Bassic_word(name['word'], name['subwords'])
        return word2


