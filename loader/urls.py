from django.urls import path

from loader.views import LoadDataAPIView, GetBillsAPIVIew

urlpatterns = [
    path('load/', LoadDataAPIView.as_view()),
    path('bills/', GetBillsAPIVIew.as_view()),
]
