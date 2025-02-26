# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first (to leverage Docker cache)
COPY requirements.txt .

# Upgrade pip to avoid dependency issues
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Ensure all Python files are readable and executable
RUN chmod -R 755 /app

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Define the command to run the app
CMD ["python", "app.py"]
