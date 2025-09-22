import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

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
    quality = model[0].predict([
        [data.fixed_acidity, data.volatile_acidity, data.citric_acid,
         data.residual_sugar, data.chlorides, data.free_sulfur_dioxide,
         data.total_sulfur_dioxide, data.density, data.pH, data.sulphates, data.alcohol]
                            ])
    return {"quality": quality[0]}

@app.post("/update-model")
def update_model(data: ModelInput):
    model[0] = mlflow.pyfunc.load_model(data.model)
    return {"message": "Model updated."}