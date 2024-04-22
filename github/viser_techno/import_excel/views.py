from django.shortcuts import render
import json

# Create your views here.
from rest_framework import generics
from .models import Person
from .serializers import DataUploadserializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import openpyxl
from rest_framework import status


# class ExcelDataCreateView(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = DataUploadserializer


class ExcelDataUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, format=None):
        try:
            file_obj = request.FILES['file']
            if not file_obj.name.endswith('.xlsx'):
                return Response({'error': 'only Xlsx file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
            wb = openpyxl.load_workbook(file_obj)
            sheet = wb.active
            excel_data_list = []

            for row in sheet.iter_rows(min_row=2, values_only=True):
                name, gender, age, country = row
                excel_data = Person(name=name, gender=gender,
                                    age=age, country=country)
                excel_data_list.append(excel_data)
            obj_list = Person.objects.bulk_create(excel_data_list)
            data = [{"name": obj.name, "gender": obj.gender,
                     "age": obj.age, "country": obj.country} for obj in obj_list]
            return Response({'message': 'Data uploaded', 'data': data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
