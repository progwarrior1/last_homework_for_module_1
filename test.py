# import random
#
# import requests
#
# from basicclass import Bassic_word
#
import json
def load_questions():
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data
n = load_questions()

# print(type(n))
#
# # def load_random_file(word):
# #     """
# #
# #     :type word: object
# #     """
# #     # data = {"word": "строка",
# #     #         "subwords": ["aкp", "aкт", "кот", "рак", "oрk", "оca", "сок", "ток", "тор", "кopa", "косa", "сота", "торc",
# #     #                      "рoca", "cкат"]
# #     #         }
# #     # word = Bassic_word(data['word'], data['subwords'])
# #     word2 = []
# #     for name in word:
# #         word2.append(Bassic_word(name['word'], name['subwords']))
# #     return word2
# # print(load_random_file(word_list))
for name in n:
    print(name['word'], ' '.join(name['subwords']))