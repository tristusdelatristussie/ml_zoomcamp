import requests
url = "http://www.127.0.0.1.com:9696/predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
requests.post(url, json=client)