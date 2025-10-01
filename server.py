import mlflow
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import numpy as np

app = FastAPI()
mlflow.set_tracking_uri("http://localhost:5000")

# Store data for our server
class ServerData():
    def __init__(self):
        self.current_model = None
        self.next_model = None
        self.proba = 0.8

server_data = ServerData()

class WineInput(BaseModel):
    fixed_acidity: float = Field(..., alias="fixed acidity")
    volatile_acidity: float = Field(..., alias="volatile acidity")
    citric_acid: float = Field(..., alias="citric acid")
    residual_sugar: float = Field(..., alias="residual sugar")
    chlorides: float
    free_sulfur_dioxide: float = Field(..., alias="free sulfur dioxide")
    total_sulfur_dioxide: float = Field(..., alias="total sulfur dioxide")
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
    """
    Takes a WineInput as argument and uses the model to make the prediction.
    """
    df = pd.DataFrame([data.model_dump(by_alias=True)])

    # If another model is set up, use canary deployment to call it
    if np.random.rand() > server_data.proba and server_data.next_model != None:
        quality = server_data.next_model.predict(df)
    else:
        quality = server_data.current_model.predict(df)
    return {"quality": float(quality[0])}

@app.post("/update-model")
def update_model(data: ModelInput):
    """
    Takes a ModelInput and update the next model.
    This model will now be used by the *predict* endpoint.
    """
    server_data.next_model = mlflow.pyfunc.load_model(data.model)
    return {"message": "Next model updated."}

@app.post("/accept-next-model")
def accept_next_model():
    """
    The next model has been tested and accepted.
    It now becomes the main model.
    """
    server_data.current_model = server_data.next_model
    return {"message": "Current model updated."}
