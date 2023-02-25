from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>Я чайник</body>")
