## Installation

For non-linux devices it's easier to run the project outside of docker:
- use python3.9
- `poetry install`
- `docker-compose up db`
- `python manage.py migrate`
- `python manage.py runserver`

If `.env` overrides are needed create an `.env.local` file.

Docker usage:

`docker-compose up app`

To connect to the running instance: `docker-compose run --rm app bash` 

## Testing

`python manage.py test --keepdb`

## Formatting

`black . && isort .`

## Poetry export for docker

`poetry export --without-hashes --format requirements.txt --output requirements.txt`

This is a temporal solution since poetry is a bit hard to install in docker. Later on we can either
migrate to pip-tools or create a base docker image with poetry.
