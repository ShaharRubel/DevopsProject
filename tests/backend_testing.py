import requests
import json
import pymysql
import time

def connect_db():
    retry_flag = True
    while retry_flag:
        try:
            connection = 0
            timeout = 10
            connection = pymysql.connect(
                charset="utf8mb4",
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                db="Devops",
                host="localhost",
                password="devops",
                read_timeout=timeout,
                port=3306,
                user="devops",
                write_timeout=timeout,
            )
            print(connection)
            return connection
        except Exception as e:
            print(e)
            time.sleep(3)



# Secure connection to db
connection = connect_db()
cursor = connection.cursor()

# Step 1. Post request to create user
url = "http://127.0.0.1:5000/users/1"

try:
    data = {"user_name": "john"}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
except:
    raise Exception("Test Failed")

# Step 2
try:
    data = requests.get(url)
    data = data.json()
    print(data['user_name'])

    if data['user_name'] == "john":
        print("test is successful")
    else:
        raise Exception("Test Failed")
except:
    print("operation failed")


# Step 3
# connect to DB

cursor.execute("SELECT * FROM Devops.users WHERE user_id = 1;")
name = cursor.fetchall()[0]['user_name']

if name == "john":
    print("test is successful")
else:
    raise Exception("Test Failed")
connection.close()