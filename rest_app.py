from flask import Flask, request, jsonify
from db_connector import connect_db, create_table
import datetime
import os
import signal
app = Flask(__name__)


@app.route('/stop_server')
def stop_server():
    # kill flask process
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

@app.route('/')
def hello_world():
    # route for monitoring uptime
    return 'Hello World'

# Handle POST
@app.route('/users/<id>', methods=['POST'])
def users_post(id):
    # print(content)
    # print(id)
    try:
        # get content of body from request
        content = request.json
        # connect to DB
        connection = connect_db()
        cursor = connection.cursor()
        print(connection)
        # Get timedate
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Query to insert with parameters
        cursor.execute(f"INSERT INTO Devops.users (user_id, user_name, creation_date)"
                            f" VALUES ('{id}', '{content['user_name']}', '{current_time}')")
        # commit changes to database - error out if id is already found
        connection.commit()

        return {"status": "ok", "user_added": content['user_name']}, 200
    except Exception as e:
        print(e)
        return {"status": "error", "reason": "id already exists"}, 500
    finally:
        connection.close()


# Handle GET
@app.route('/users/<id>', methods=['GET'])
def users_get(id):
    try:
        # connect to DB
        connection = connect_db()
        cursor = connection.cursor()
        # load a query to get all content where user_id matches id from request
        cursor.execute(f"SELECT * FROM Devops.users WHERE user_id = {id};")
        # fetch data from the query above
        data = cursor.fetchall()

        return {"status": "ok", "user_name": data[0]["user_name"] }, 200
    except:
        return {"status": "error", "reason": "no such id"}, 500
    finally:
        connection.close()


# Handle PUT
@app.route('/users/<id>', methods=['PUT'])
def users_put(id):
    try:
        # Get body content from request
        content = request.json['user_name']
        # connect to DB
        connection = connect_db()
        cursor = connection.cursor()

        # Check if id doesn't exist, enter else if id doesn't exist
        if cursor.execute(f"SELECT * FROM Devops.users WHERE user_id = {id};"):
            # Update user_name where id matches user_id
            cursor.execute(f"UPDATE Devops.users SET user_name= '{content}' "
                           f"WHERE user_id = {id}")
            # commit changes from the query above
            connection.commit()
        else:
            # raise error if the query returns empty
            raise ValueError("Error: ID does not exist in the database.")

        return {"status": "ok", "user_updated": content}, 200
    except Exception as e:
        print(e)
        return {"status": "error", "reason": "no such id"}, 500
    finally:
        connection.close()


# Handle DELETE
@app.route('/users/<id>', methods=['DELETE'])
def users_delete(id):
    try:
        # connect to DB
        connection = connect_db()
        cursor = connection.cursor()
        # Check if id matches any user_id
        if cursor.execute(f"SELECT * FROM Devops.users WHERE user_id = {id};"):
            # Delete row with user_id matching id
            cursor.execute(f"DELETE FROM Devops.users WHERE user_id = {id}")
            connection.commit()
        else:
            # Raise error if ID doesn't exist
            raise ValueError("Error: ID does not exist in the database.")

        return {"status": "ok", "user_deleted": id}, 200
    except:
        return {"status": "error", "reason": "no such id"}, 500
    finally:
        connection.close()



if __name__ == '__main__':
    # init table
    create_table()

    app.run(host='0.0.0.0', debug=True, port=5000)