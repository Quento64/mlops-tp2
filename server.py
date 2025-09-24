import mlflow
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
mlflow.set_tracking_uri('http://localhost:5000')

model = [None]

class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

class ModelInput(BaseModel):
    model: str

@app.get("/")
def root():
    return {"message": "Welcome to the white whine quality AI."}

@app.post("/predict")
def predict(data: WineInput):
    data_dict = {
        "fixed_acidity": data.fixed_acidity,
        "volatile_acidity": data.volatile_acidity,
        "citric_acid": data.citric_acid,
        "residual_sugar": data.residual_sugar,
        "chlorides": data.chlorides,
        "free_sulfur_dioxide": data.free_sulfur_dioxide,
        "total_sulfur_dioxide": data.total_sulfur_dioxide,
        "density": data.density,
        "pH": data.pH,
        "sulphates": data.sulphates,
        "alcohol": data.alcohol,
        "quality": 0
    }

    df = pd.DataFrame(data_dict)
    quality = model[0].predict(df)
    return {"quality": quality[0]}

@app.post("/update-model")
def update_model(data: ModelInput):
    model[0] = mlflow.pyfunc.load_model(data.model)
    return {"message": "Model updated."}