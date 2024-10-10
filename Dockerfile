# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy the current directory contents into the container
COPY . /home/data

# Install any dependencies from a requirements.txt file (if you have one)
# RUN pip install --no-cache-dir -r requirements.txt

# If you don't have a requirements.txt file, skip the above and use this
# to install your specific packages (optional)
# RUN pip install --no-cache-dir <your-python-package>

# Run a simple Python script (replace app.py with your script)
CMD ["python", "app.py"]

