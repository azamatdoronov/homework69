import json

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


def index_view(request):
    return render(request, 'index.html')


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def math_action(request):
    body = json.loads(request.body)
    action = request.META.get('PATH_INFO').strip('/')
    a = str(body.get('a'))
    b = str(body.get('b'))
    if not a.isdigit():
        response = JsonResponse({'error': f'{a}  not integer'})
        response.status_code = 400
        return response
    if not b.isdigit():
        response = JsonResponse({'error': f'{b} not integer'})
        response.status_code = 400
        return response
    if action == 'add':
        c = int(a) + int(b)
        answer = {'answer': c}
        return JsonResponse(answer)
    if action == 'subtract':
        c = int(a) - int(b)
        answer = {'answer': c}
        return JsonResponse(answer)
    if action == 'multiply':
        c = int(a) * int(b)
        answer = {'answer': c}
        return JsonResponse(answer)
    if action == 'divide':
        if int(b) == 0:
            response = JsonResponse({'error': 'zero division error'})
            response.status_code = 400
            return response
        else:
            c = int(a) / int(b)
            answer = {'answer': c}
            return JsonResponse(answer)
