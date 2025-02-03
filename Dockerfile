# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the project files
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
