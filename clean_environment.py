import requests

try:
    # stop rest_app.py
    requests.get('http://127.0.0.1:5000/stop_server')
    requests.get('http://127.0.0.1:5000/stop_server')
except:
    pass

try:
    # step web_app.py
    requests.get('http://127.0.0.1:5001/stop_server')
    requests.get('http://127.0.0.1:5001/stop_server')
except:
    pass