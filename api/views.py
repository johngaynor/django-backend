from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
import json
import csv

# Create your views here.
# request -> returns response (request handler, action)


def csrf(request):
    return render(request, 'csrf_token_page.html')


def test_post(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if data is not None:
            return JsonResponse({'data': data['data']})
        else:
            return JsonResponse({'error': 'Parameter "data" not found in the request'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def test_get(request):
    return JsonResponse({'success': 'get route works'})


def init_upload(request):
    if request.FILES:
        uploaded_file = request.FILES['csv_file']
        transactions = []
        decoded_file = uploaded_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            transactions.append(row)

        return JsonResponse({'transactions': transactions})
    else:
        return JsonResponse({'msg': 'Invalid file format. Please upload a CSV file.'}, status=400)


# files can be accessed via request.FILES.['filename]
# params accessed via request.GET, which returns a dictionary of all parameters
