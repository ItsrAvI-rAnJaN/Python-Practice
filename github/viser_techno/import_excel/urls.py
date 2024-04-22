from django.urls import path
from .views import ExcelDataUploadView
# from .views import ExcelDataUploadView,ExcelDataCreateView



urlpatterns = [
    # path('excel_create/', ExcelDataCreateView.as_view(), name='excel_data_create'),
    path('excel_upload/',ExcelDataUploadView.as_view(), name='excel_data_upload')
]
