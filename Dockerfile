# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy the current directory contents into the container
COPY . /home/data

# Install required package
RUN pip install --no-cache-dir contractions

# Run the script with python
CMD ["python", "app.py"]
