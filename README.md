# wingz-django-assessment

## Installing dependencies

1. Install poetry by running `pip install poetry`
2. Run `poetry install` to install dependencies

## Running the API

1. Run `poetry shell`
2. Create and populate .env file

```shell
cp .env.example .env
```

3. Run `python manage.py migrate` to apply database migrations
    - Run `python manage.py generate_users` to create test instances for users
    - Run `python manage.py generate_rides` to create test instances for rides and ride events
4. Create an admin/superuser for API access by running `python manage.py createsuperuser` 
5. Start the development server by executing `python manage.py runserver`


## Testing on Postman

- Join workspace through link: https://app.getpostman.com/join-team?invite_code=1ef4b310531b93c33427cf9e033e945d1418fba9696d6850fa0f4948cb9ac992&target_code=fe4525ec14f0719d3341b3e126a1fefd
- Workspace includes requests for the required endpoints for the assessment
  - ![postman](https://github.com/user-attachments/assets/8527ec7c-2c10-4c74-a770-4e9b841d3321)


## Query Optimization

- Django debug toolbar indicates additional queries for users that are not included in the endpoint
    - ![toolbar results](https://github.com/user-attachments/assets/512fbc50-3fef-45c6-807a-4dc0d450bf5a)
- Middleware for query count and printing has been added to verify results from Django Debug Toolbar
    - ![middleware results](https://github.com/user-attachments/assets/bdf91a3b-3051-4628-801b-beee8b7c0741)
    - The first 3 queries are due to authentication while the remaining 3 are queries for the pagination, rides and ride events
