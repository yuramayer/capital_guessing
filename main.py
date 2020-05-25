# -*- coding: utf-8 -*-
import answer
import json_data
import random

data = json_data.data

user = {}


def is_english(string):
    """Checking string on non-english elements"""
    try:
        string.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def get_rand_country():
    """Getting random country without non-english elements"""
    rand_country_dict = random.choice(data)
    if is_english(rand_country_dict['country']):
        if is_english(rand_country_dict['capital']):
            return rand_country_dict
    return get_rand_country()


def greetings():
    """Getting username and creating user dict"""
    name = input('Hello! What\'s your name?\n')
    user['name'] = name
    user['points'] = 0
    print('Nice to meet you, ' + user['name'] + '!')


def begin():
    """Menu"""
    lets_start = input('Let\'s play, ' + user['name'] + '! Type me \'yes\' or \'no\'\n')
    if answer.is_yes(lets_start):
        return True
    elif answer.is_no(lets_start):
        input('When you would like to play, just type me!\n')
        return begin()
    else:
        input('Please, type \'yes\' or \'no\'. '
              'I\'m trying to be smart, but it\'s so hard to understand words!\n')
        return begin()


def whats_game():
    """Choosing game"""
    game = input('Would you like to guess capitals or countries?\n')
    if answer.is_capitals(game):
        print('I\'m in love with guessing capitals!')
        capital_game()
    elif answer.is_countries(game):
        print('Love this game!')
        countries_game()
    else:
        print('Please, choose the game! Type me \'capitals\' or \'countries\'')
        whats_game()


def capital_game():
    """Game with guessing capitals"""
    rand_country_dict = get_rand_country()
    user_capital = input('What is the capital of ' + rand_country_dict['country'] + '?\n')
    if answer.is_right_capital(user_capital, rand_country_dict):
        user['points'] += 2
        print('You are right! Add 2 points. You\'ve got', user['points'], 'points!\n')
    elif answer.is_mistake_capital(user_capital, rand_country_dict):
        user['points'] += 1
        print('Well, but the capital is: ' + rand_country_dict['capital'] +
              '!\nAdd 1 point. You\'ve got ', user['points'], 'points!\n')
    else:
        print('No, it\'s ' + rand_country_dict['capital'] + '!\n')

    capital_game()


def countries_game():
    """Game with guessing countries"""
    rand_country_dict = get_rand_country()
    user_country = input('What is the country with the capital ' + rand_country_dict['capital'] + '?\n')
    if answer.is_right_country(user_country, rand_country_dict):
        user['points'] += 2
        print('You are right!\nAdd 2 points. You\'ve got ', user['points'], 'points!\n')
    elif answer.is_mistake_country(user_country, rand_country_dict):
        user['points'] += 1
        print('Well, but the country is: ' + rand_country_dict['country'] +
              '!\nAdd 1 point. You\'ve got', user['points'], 'points!\n')
    else:
        print('No, it\'s ' + rand_country_dict['country'] + '!\n')

    capital_game()


while True:
    greetings()
    if begin():
        whats_game()

