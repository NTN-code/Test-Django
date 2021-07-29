import datetime


class SaveUsernameMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_user = datetime.datetime.now()
        request_method = request.META.get("REQUEST_METHOD")
        request_server_MAC_address = request.META.get("SERVER_NAME")
        request_url = request.get_full_path()
        with open('username.txt', 'a', encoding='UTF-8') as w_file:
            line = f'[{time_user}]--[{request_method}]--[{request_server_MAC_address}]--[{request_url}]\n'
            w_file.write(line)

        response = self.get_response(request)
        return response
