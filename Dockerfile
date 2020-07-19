FROM python:3.8.4-slim-buster
WORKDIR /opt/webapp
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "dateapp:app"]