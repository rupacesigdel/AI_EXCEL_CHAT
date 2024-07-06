import requests

try:
    response = requests.get('http://127.0.0.1:47334')
    print("MindsDB is running. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error connecting to MindsDB:", str(e))