from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Siemanko to jest testowa odpowiedź serwera"})
