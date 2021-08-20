FROM python:3.9-buster

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-deps --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir /app/static_collected
RUN DJANGO_ENV="build_docker" python manage.py collectstatic --no-input

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--worker-class=uvicorn.workers.UvicornWorker", "eahub.asgi:application"]
