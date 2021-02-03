# Define use image
FROM python:3.8.3-alpine

ENV APP_HOME=/easybank

# Create directory for the app user. This line can be avoid dir permissions issues
RUN mkdir -p $APP_HOME

# Specify work directory
WORKDIR $APP_HOME

# Keeps Python from generating .pyc files in the container
ENV PYTHONUNBUFFERED=1

# Turns off buffering for easier container logging
ENV PYTHONDONTWRITEBYTECODE=1

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy files to work directory
COPY ./postgres-healthy.sh ./

COPY ./ ./

# Run postgres-healthy.sh
ENTRYPOINT ["./postgres-healthy.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]