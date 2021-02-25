from flask import Flask, url_for, render_template, request
from projects.roman import convert_to_roman
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html.jinja')

@app.route('/roman-converter')
def romanConverter():
    converterNumber = None
    number = request.args.get('number', type = int)
    if number:
        converterNumber = convert_to_roman(number)
    return render_template('roman_converter.html.jinja', inputNumber=number, convertedNumber=converterNumber)

@app.route('/guess-number')
def guessNumber():
    return render_template('guess_number.html.jinja')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# with app.test_request_context():
#     print(url_for('home'), flush=True)
#     print(url_for('quiz'), flush=True)