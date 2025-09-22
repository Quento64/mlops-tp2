import requests

url = "http://127.0.0.1:8000/update-model"

data = {
    "model": "models:/m-b41bbe0197f14bb8b48d151622ba25f5"
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response JSON:", response.json())

url = "http://127.0.0.1:8000/predict"

data = {
    "fixed_acidity": 4.9,
    "volatile_acidity": 0.41,
    "citric_acid": 0.32,
    "residual_sugar": 10,
    "chlorides": 0.043,
    "free_sulfur_dioxide": 123,
    "total_sulfur_dioxide": 194,
    "density": 1.008,
    "pH": 2.9,
    "sulphates": 0.42,
    "alcohol": 6,
}
response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
