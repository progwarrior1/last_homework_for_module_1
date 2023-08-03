from utils import load_random_file, load_questions
import random
from basicclass import Player

n = load_questions()
random.shuffle(n)


def main():
    print('привет, представтесь пожалуйста')
    player_input = input()
    player_info = Player(player_input)
    main_word = load_random_file(n)
    word = main_word.value
    subword = main_word.count_subwords()
    print(f'составьте {subword} слов из слова {word}')
    print('введи слово')
    game_is_on = True
    while player_info.count_of_used() != main_word.count_subwords():
        user_input = input()
        if player_info.check_used(user_input):
            print('уже писали это слово')
            continue
        if len(user_input) < 3:
            print('слишком короткий ответ')
            continue
        if user_input == 'стоп' or user_input == 'stop':
            break
        if main_word.check_input(user_input):
            print('слово есть')
            player_info.add_to_used(user_input)
        elif not main_word.check_input(user_input):
            print('слова нет')
    print(f'игра завершена вы угадали {player_info.count_of_used()}')


main()
