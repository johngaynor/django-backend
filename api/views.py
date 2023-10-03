from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# request -> returns response (request handler, action)


def say_hello(request):
    try:
        if request.method == 'POST' and 'csv_file' in request.FILES:
            uploaded_file = request.FILES['csv_file']

            # handle sorting operations
            return JsonResponse({'success': 'csv has been processed'})
        else:
            return JsonResponse({'error': 'Invalid request'})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def test_get(request):
    return JsonResponse({'success': 'get route works'})


def home(request):
    return render(request, 'hello.html', {'name': 'John'})


def auto_category(request):
    if request.method == 'POST' and 'csv_file' in request.FILES:
        uploaded_file = request.FILES['csv_file']

        # handle sorting operations
        return JsonResponse({'success': 'csv has been processed'})
    else:
        return JsonResponse({'error': 'Invalid request'})


# files can be accessed via request.FILES.['filename]
# params accessed via request.GET, which returns a dictionary of all parameters
