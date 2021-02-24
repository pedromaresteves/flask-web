from flask import Flask, url_for, render_template, request
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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def convert_to_roman(num):
    result = {'value': '', 'validInput': False}
    resultMaker = ''
    poops = {
    "M":1000,
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40,
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
    }
    try:
        if num <= 0:
            return result
        for item in poops:
            while(num >= poops[item]):
                result['value'] += item
                num = num - poops[item]
    except:
        return result
    result['validInput'] = True
    return result


    # with app.test_request_context():
#     print(url_for('home'), flush=True)
#     print(url_for('quiz'), flush=True)