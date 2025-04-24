import requests
import json
import sys
import os

# Importing from parent directory setup
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from db_connector import connect_db


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
connection = connect_db()
cursor = connection.cursor()
cursor.execute("SELECT * FROM Devops.users WHERE user_id = 1;")
name = cursor.fetchall()[0]['user_name']

if name == "john":
    print("test is successful")
else:
    raise Exception("Test Failed")
connection.close()