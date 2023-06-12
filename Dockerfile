FROM python:3.11

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

CMD ["python", "jarvis.py"]