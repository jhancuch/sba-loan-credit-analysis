FROM python:3.9-slim

# Install libraries
COPY ./requirements.txt ./
RUN pip install -r requirements.txt && \
    rm ./requirements.txt

# Setup container directories
RUN mkdir /app

# Copy local code to the container
COPY ./app /app

# launch server with gunicorn
WORKDIR /app
EXPOSE 1234
CMD ["gunicorn", "main:app", "--timeout=30", "--workers=1", "--threads=4", "--preload", "--bind=0.0.0.0:1234"]