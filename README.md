# MLOPS TP2

This repository is the submission of the TP2 of the mlops course.

It shows the basics of MLflow and canary deployment.

---

## How to use

1. Create environment and install depedencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Start the MLflow server

```bash
mlflow server --host 127.0.0.1 --port 5000
```

3. Create a model and store it in mlflow (the model is created in **create_model.py**)

```bash
python3 create_model.py
```

You can now view the model by going to [MLflow dashboard](http://localhost:5000).

4. Start the FastAPI server

```bash
fastapi dev server.py
```

You can also use the provided **docker-compose.yml** file.

```bash
docker-compose up
```

5. Test the server

```bash
python3 test_server.py
```
