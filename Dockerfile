# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python and Docker
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

RUN pip3 install gunicorn

#RUN chown -R node /app/node_modules

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 to allow outside requests
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate

# Define the default command to run when the container starts

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

