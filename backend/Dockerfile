FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=rest_app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python", "rest_app.py"]