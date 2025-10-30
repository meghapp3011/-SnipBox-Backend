FROM python:3
ENV PYTHONUNBUFFER 1
WORKDIR /app

WORKDIR /app
# copy requirements file
COPY requirements.txt /app/
# Install Python dependencies
RUN pip install -r requirements.txt

COPY . /app/

# Expose port
EXPOSE 8000

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
