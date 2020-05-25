from difflib import get_close_matches as g_c_m, SequenceMatcher

yes_ans_tuple = ('yes', 'yeah', 'yep', 'ok', 'k', 'good', 'well', '+', '1')

no_ans_tuple = ('no', 'not', 'dont', 'don\'t', 'do not', 'n', 'bad', '-', '0')


def is_yes(answer):
    """True if answer looks like 'yes'"""
    if g_c_m(answer.lower(), yes_ans_tuple):
        return True


def is_no(answer):
    """True if answer looks like 'no'"""
    if g_c_m(answer.lower(), no_ans_tuple):
        return True


def is_capitals(answer):
    """True if looks like user chose 'capitals' game"""
    similarity = SequenceMatcher(None, answer, 'capitals').ratio()
    if similarity > 0.7:
        return True


def is_countries(answer):
    """True if looks like user chose 'countries' game"""
    similarity = SequenceMatcher(None, answer, 'countries').ratio()
    if similarity > 0.7:
        return True


def is_right_capital(user_capital, rand_country_dict):
    """True if user guessed the capital"""
    if user_capital == rand_country_dict['capital']:
        return True


def is_mistake_capital(user_capital, rand_country_dict):
    """True if looks like user guessed the capital"""
    similarity = SequenceMatcher(None, user_capital, rand_country_dict['capital']).ratio()
    if similarity > 0.7:
        return True


def is_right_country(user_country, rand_country_dict):
    """True if user guessed the country"""
    if user_country == rand_country_dict['country']:
        return True


def is_mistake_country(user_country, rand_country_dict):
    """True if looks like user guessed the country"""
    similarity = SequenceMatcher(None, user_country, rand_country_dict['country']).ratio()
    if similarity > 0.7:
        return True

