import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#  Print out Hello world
@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World!</h1><p>View games with Python and Flask!</p>"

#  Form to get game and developer
@app.route('/api/movies/add', methods=['POST'])
def api_add():
    game = request.form['game']
    developer = request.form['developer']
    try:
        connection = psycopg2.connect(user="j.lin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="python_flask")
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        print(game, developer)
        insertQuery = "INSERT INTO games (game, developer) VALUES (%s, %s)"

        # pool.query
        cursor.execute(insertQuery, (game, developer))

        connection.commit()
        count = cursor.rowcount
        print(count, "Game Added")

        result = {'status': 'CREATED'}
        return make_response(jsonify(result), 201)
    except (Exception, psycopg2.Error) as error:
        # there was a problem
        if(connection):
            print("Failed to insert book", error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        # closing database connection.
        if(connection):
            # clean up our connections
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


#  Return all games
@app.route('/api/games/all', methods=['GET'])
def api_all():
    connection = psycopg2.connect(user="j.lin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="prime_flask")

    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM games"

    # execute query
    cursor.execute(postgreSQL_select_Query)
    # Selecting rows from mobile table using cursor.fetchall
    books = cursor.fetchall()
    # respond, status 200 is added for us
    return jsonify(games)

app.run()