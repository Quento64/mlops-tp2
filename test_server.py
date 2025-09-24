import requests

url = "http://127.0.0.1:8000/update-model"

data = {
    "model": "models:/m-189d69765c064445a5f5483414c94330"
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response JSON:", response.json())

url = "http://127.0.0.1:8000/predict"

data = {
    "fixed_acidity": [4.9],
    "volatile_acidity": [0.41],
    "citric_acid": [0.32],
    "residual_sugar": [10.0],
    "chlorides": [0.043],
    "free_sulfur_dioxide": [123.0],
    "total_sulfur_dioxide": [194.0],
    "density": [1.008],
    "pH": [2.9],
    "sulphates": [0.42],
    "alcohol": [6.0],
    "quality": [0]
}
response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
