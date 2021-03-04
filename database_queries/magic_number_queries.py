import psycopg2
import os

db_connection_creds = {'user':os.environ['DB_USER'], 'password':os.environ['DB_PASSWORD'],
'host':os.environ['DB_HOST'], 'port':os.environ['DB_PORT'], 'database':os.environ['DB_DATABASE']}

def create_new_game(username, magic_number):
    new_game_info = {'game_id': None, 'username': username}
    try:
        connection = psycopg2.connect(**db_connection_creds)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO magic_number (id, username, magic_number, number_of_tries, game_over) VALUES (default, '{username}', {magic_number}, 0, False)")
        cursor.execute("SELECT * FROM magic_number ORDER BY id DESC")
        record = cursor.fetchone()
        new_game_info['game_id'] = record[0]
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        cursor.close()
        connection.close()
        print('Postgres is closed')
    return new_game_info

def get_game_info(game_id):
    connection = psycopg2.connect(**db_connection_creds)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM magic_number WHERE id = {game_id}")
    record = cursor.fetchone()
    cursor.close()
    connection.close()
    game_data = {'game_id': record[0], 'username': record[1],'magic_number': record[2],
    'number_of_tries': record[3], 'last_mistake': record[4], 'last_guess': record[5],
    'game_status': record[6], 'game_over': record[7]}
    return game_data

def update_game_info(game_id, game_data):
    connection = psycopg2.connect(**db_connection_creds)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(f"UPDATE magic_number SET game_status = '{game_data['game_status']}', last_guess = {game_data['last_guess']}, last_mistake = '{game_data['last_mistake']}', number_of_tries = {game_data['number_of_tries']}, game_over = '{game_data['game_over']}' WHERE id = {game_id};")
    cursor.close()
    connection.close()
    return