# flask-web

## How to work in the project:
1. Enter project folder and activate the virtual environment by typing the following command: `$ . venv/Scripts/activate`
2. Install all required packages: `$ pip3 install -r requirements.txt`
3. If you install new packages afterwards make sure to update the requirements.txt: `$ pip3 freeze > requirements.txt`

## Run unit tests
To run unit tests execute the following command (doesn't work in powershell): `$ python -m unittest discover projects/unittests`

## How to run the app
### How to run the app in development mode
1. Export the FLASK_ENV variable and assign it 'development': `$ export FLASK_ENV=development`

### Run App
1. First you have to export de FLASK_APP variable and assign it the app.py file: `$ export FLASK_APP=app.py`
2. Run the command: `$ flask run`