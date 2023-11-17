FROM python:3.8
WORKDIR /api-publisher
COPY ./requirements.txt /api-publisher/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /api-publisher/requirements.txt
COPY . /api-publisher
CMD ["uvicorn", "publisher:app", "--host", "0.0.0.0", "--port", "8000"]