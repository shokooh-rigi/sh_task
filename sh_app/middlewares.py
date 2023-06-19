from django.http import JsonResponse


class InvalidRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # if request.method != 'POST':
        #     return JsonResponse({'message': 'Only POST requests are allowed.'}, status=400)

        # if request.content_type != 'application/json':
        #     return JsonResponse({'message': 'Only JSON format is allowed.'}, status=400)

        response = self.get_response(request)
        return response
