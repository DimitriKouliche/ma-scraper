# MA Scrapper

This project scraps a well-known website.

## How to install me

- Make sure you have python 3 and git installed on your system
- Clone the project: `git clone https://github.com/DimitriKouliche/ma-scrapper.git` 
- Install pipenv: `pip install pipenv`
- Retrieve dependencies: `pipenv install` (if you plan on developing use `pipenv install --dev` instead)
- Copy .env.dist and rename it .env, update values in it accordingly (database connection)

## Run the project

- Activate virtual environment by running `pipenv shell`
- Load database migrations: `PYTHONPATH=. alembic upgrade head`
- Run the project: `python .`