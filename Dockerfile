FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY splitter.py .

CMD [ "python", "splitter.py" ]
