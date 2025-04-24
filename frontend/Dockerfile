FROM python:3.13-slim
WORKDIR /app
COPY .. /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
ENV FLASK_APP=web_app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python", "web_app.py"]