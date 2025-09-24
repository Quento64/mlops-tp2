FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py server.py

EXPOSE 5000

CMD ["fastapi",  "dev", "server.py"]
