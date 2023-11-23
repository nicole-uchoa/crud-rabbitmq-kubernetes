FROM python:3.8
WORKDIR /db-receiver
COPY ./requirements.txt /db-receiver/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /db-receiver

CMD [ "python3", "db-receiver.py" ]