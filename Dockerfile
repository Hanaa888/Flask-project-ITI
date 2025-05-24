FROM python:3.10-slim
COPY . /application
WORKDIR /application
RUN pip install flask
CMD ["python", "routes.py"]
