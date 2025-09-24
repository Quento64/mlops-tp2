import requests

url = "http://127.0.0.1:8000/update-model"

data = {
    "model": "models:/whine_quality/1"
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response JSON:", response.json())

url = "http://127.0.0.1:8000/accept-next-model"

data = {
    "model": "models:/whine_quality/1"
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response JSON:", response.json())

url = "http://127.0.0.1:8000/predict"

data = {
    "fixed acidity": 4.9,
    "volatile acidity": 0.41,
    "citric acid": 0.32,
    "residual sugar": 10.0,
    "chlorides": 0.043,
    "free sulfur dioxide": 123.0,
    "total sulfur dioxide": 194.0,
    "density": 1.008,
    "pH": 2.9,
    "sulphates": 0.42,
    "alcohol": 6.0
}
response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())