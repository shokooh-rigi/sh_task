from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled
from rest_framework.response import Response


class IncorrectRequestThrottle(SimpleRateThrottle):
    scope = 'incorrect_requests'

    def allow_request(self, request, view):
        if request.method.lower() not in ('post', 'put', 'patch', 'delete'):
            return True
        if request.content_type != 'application/json':
            return True

        return super().allow_request(request, view)


def custom_exception_handler(exc, context):
    if isinstance(exc, Throttled):
        response = Response({'error': 'You have exceeded the rate limit for incorrect requests. Please try again later.'})
        response.status_code = 429
        return response
    return None
