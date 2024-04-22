# from django.shortcuts import render
#
# # Create your views here.
# import json
# from django.db import connection
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher


@csrf_exempt
def csv_to_db(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        content = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(content)
        rows = list(reader)
        for row in rows:
            Teacher.objects.create(teacher_id=row['teacher_id'], subject_id=row['subject_id'], dept_id=row['dept_id'])

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

