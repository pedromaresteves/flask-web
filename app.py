from flask import Flask, url_for, render_template, request, redirect
from random import randint
from projects.roman import convert_to_roman
from projects.magic_number import guess_number, validate_username
from database_queries.magic_number_queries import create_new_game, get_game_info
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html.jinja')

@app.route('/roman-converter/')
def romanConverter():
    converterNumber = None
    number = request.args.get('number', type = int)
    if number:
        converterNumber = convert_to_roman(number)
    return render_template('roman_converter.html.jinja', inputNumber=number, convertedNumber=converterNumber)

@app.route('/magic-number/', methods=['GET', 'POST'])
def guessNumberHome():
    username_is_valid = True
    if request.method == 'POST':
        magic_number = randint(1, 10)
        escaped_username = escape(request.form['username'])
        username_is_valid = validate_username(escaped_username)
        if username_is_valid:
            new_game = create_new_game(escaped_username, magic_number)
            return redirect(url_for('guessNumberGame', game_id=new_game['game_id'], username=new_game['username']))
    return render_template('magic_number_home.html.jinja', username_is_valid=username_is_valid)


@app.route('/magic-number/<int:game_id>/<string:username>', methods=['GET', 'POST'])
def guessNumberGame(game_id, username):
    guess = None
    result = None
    error = None
    escaped_username = escape(username)
    game_data = get_game_info(game_id)
    print(game_data, 'FUCK', flush=True)
    last_guess = game_data['last_guess']
    mistake = game_data['last_mistake']
    tries_remaining = 5 - game_data['number_of_tries']
    magic_number = game_data['magic_number']
    game_over = game_data['game_over']
    game_status = game_data['game_status']
    if request.method == 'POST':
        guess = request.form['number']
        result = guess_number(game_id, guess, game_data)
        last_guess = result['last_guess']
        mistake = result['last_mistake']
        tries_remaining = 5 - result['number_of_tries']
        game_over = result['game_over']
        magic_number = result['magic_number']
        game_status = result['game_status']
    return render_template('magic_number_game.html.jinja',
    username=escaped_username,
    magic_number=magic_number,
    guess=guess,
    last_guess=last_guess,
    mistake=mistake,
    tries_remaining=tries_remaining,
    game_over=game_over,
    game_status=game_status)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404