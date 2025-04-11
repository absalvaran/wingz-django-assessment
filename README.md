# wingz-django-assessment

## Installing dependencies

1. Install poetry by running `pip install poetry`
2. Run `poetry install` to install dependencies

## Running the API

1. Run `poetry shell`
2. Navigate to the `/api`
3. Create .env file

```shell
cp .env.example .env
```

4. Run `python manage.py migrate` to apply database migrations
5. Start the development server by executing `python manage.py runserver`.