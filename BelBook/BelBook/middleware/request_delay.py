from time import sleep


class RequestDelayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sleep(1)
        response = self.get_response(request)
        return response

