from time import time
from django.core.exceptions import PermissionDenied


class TimeExceptionIPMiddleware:
    time1 = time()
    visited_IP = dict()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time2 = time()
        ip = request.META.get('REMOTE_ADD')
        if time2 - TimeExceptionIPMiddleware.time1 > 30:
            TimeExceptionIPMiddleware.visited_IP = dict()
            TimeExceptionIPMiddleware.time1 = time2
        else:
            if ip not in TimeExceptionIPMiddleware.visited_IP.keys():
                TimeExceptionIPMiddleware.visited_IP[ip] = 1
            else:
                TimeExceptionIPMiddleware.visited_IP[ip] += TimeExceptionIPMiddleware.visited_IP[ip]
        if TimeExceptionIPMiddleware.visited_IP[ip] < 30:
            response = self.get_response(request)
            return response
        else:
            raise PermissionDenied
