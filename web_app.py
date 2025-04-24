from flask import Flask
from db_connector import connect_db
import os
import signal


app = Flask(__name__)

@app.route('/')
def hello_world():
    # route for monitoring uptime
    return 'Hello World'

@app.route('/stop_server')
def stop_server():
    # kill flask process
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

@app.route('/users/get_user_data/<id>')
def get_user(id):
    try:
        # connect to DB
        connection = connect_db()
        cursor = connection.cursor()
        # load a query to get all content where user_id matches id from request
        cursor.execute(f"SELECT * FROM Devops.users WHERE user_id = {id};")
        # fetch data from the query above
        name = cursor.fetchall()[0]['user_name']

        return f"<H1 id='user'>{name}</H1>"
    except Exception as e:
        return f"<H1 id='error'> no such user: {id}</H1>"
        # return id
    finally:
        connection.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)