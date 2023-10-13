from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware import csrf
from django.shortcuts import render
import json

# Create your views here.
# request -> returns response (request handler, action)


def csrf(request):
    return render(request, 'csrf_token_page.html')


def test_post(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if data is not None:
            return JsonResponse({'data': data['data'] + 3})
        else:
            return JsonResponse({'error': 'Parameter "data" not found in the request'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def test_get(request):
    return JsonResponse({'success': 'get route works'})


def home(request):
    return render(request, 'hello.html', {'name': 'John'})

# files can be accessed via request.FILES.['filename]
# params accessed via request.GET, which returns a dictionary of all parameters
