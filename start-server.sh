#!/usr/bin/env bash

echo "***************  Launching MLFlow Server  ***************"

mlflow server \
    --backend-store-uri sqlite:///mlruns.db \
    --host 0.0.0.0 \
    --port 5000
