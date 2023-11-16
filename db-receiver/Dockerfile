FROM python:3.8
WORKDIR /db-receiver
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./receiver.py" ]