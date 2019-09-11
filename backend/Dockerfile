FROM python:3.6-alpine

EXPOSE 5000
ENV MONGO_URI mongodb+srv://user:pass@atlas-cluster.mongodb.net/test?retryWrites=true&w=majority
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
