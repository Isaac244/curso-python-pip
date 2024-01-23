FROM python:3.10

WORKDIR /app-csv
COPY requirements.txt /app-csv/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app-csv/requirements.txt

COPY . /app-csv/

CMD bash -c "while true; do sleep 1; done"