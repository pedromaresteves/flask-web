import random
import sys
import re
from database_queries.magic_number_queries import update_game_info

texts = {
    "correct_answer_txt" : "You did a good job!",
    "incorrect_answer_too_high_txt" : "You're too high",
    "incorrect_answer_too_low_txt" : "You're too low!",
    "exit_msg" : "Bye"
}

def convert_user_input(user_input):
    if(user_input == "exit"):
        sys.exit(texts["exit_msg"])
    try:
        return int(user_input)
    except:
        return False

def check_number(num, rand_num):
    result = {'right_guess': None, 'mistake': None}
    if (num == rand_num):
        result["right_guess"] = True
        result["mistake"] = None
    else:
        if (num > rand_num):
            result["mistake"] = 'high'
        if (num < rand_num):
            result["mistake"] = 'low'
        result["right_guess"] = False
    return result

def guess_number(game_id, guess, game_data):
    if(game_data['number_of_tries'] == 5):
        game_data['last_mistake'] = None
        game_data['invalid_try'] = True
        return game_data
    converted_user_input = convert_user_input(guess)
    if(converted_user_input and converted_user_input > 0):  
        result = check_number(converted_user_input, game_data['magic_number'])
        game_data['number_of_tries'] += 1
        game_data['last_guess'] = converted_user_input
        game_data['last_mistake'] = result['mistake']
        if (result['right_guess']):
            game_data['game_over'] = True
            game_data['game_status'] = 'victory'
        if (game_data['number_of_tries'] == 5 and result['right_guess'] == False):
            game_data['game_over'] = True
            game_data['game_status'] = 'lost'
    else:
        game_data['last_mistake'] = 'invalid'
        game_data['last_guess'] = -1
    update_game_info(game_id, game_data)
    return game_data

def validate_username(username):
    pattern = re.compile('["!"·$%&/()=?.]')
    matches = pattern.findall(username)
    is_valid = len(matches) == 0
    return is_valid