class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.all_request = 0
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        self.all_request += 1

        if self.all_request == 10:
            self.all_request = 0
            self.text = response.content.decode("UTF-8").strip("</body>")
            response.content = self.text
        # Code to be executed for each request/response after
        # the view is called.

        return response
