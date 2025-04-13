from django.conf import settings
from django.db import connection


class QueryDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.DEBUG:
            print(f"Request Path: {request.path}")
            print("Total queries:", len(connection.queries))
            for query in connection.queries:
                print(f"SQL: {query['sql']}\n")
        return response
