# Use official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project into the container
COPY . /app/

# Expose the port Django will run on
EXPOSE 8000

# Command to run Django (manage.py runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
