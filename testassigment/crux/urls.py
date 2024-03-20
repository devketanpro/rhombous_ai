from django.urls import path
from .views import CSVUploadView, RecordView

urlpatterns = [
    path('upload/', CSVUploadView.as_view(), name='crux-report'),
    path('data', RecordView.as_view(), name='data'),
]
