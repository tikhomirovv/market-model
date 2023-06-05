# We start from a base image that already has Python installed
FROM python:3.9

# Set a directory for the app
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install all the python dependencies
COPY src .
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD [ "python", "/app/main.py" ]

