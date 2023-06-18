from django.urls import path, include
from rest_framework import routers

from .views import HistoryViewSet, SumAPIView, TotalAPIView

app_name = 'sh_app'

urlpatterns = [

    path('sum/', SumAPIView.as_view(), name='sum'),
    path('total/', TotalAPIView.as_view(), name='total'),
    path('history/', HistoryViewSet.as_view(), name='history'),
    path('', include(router.urls)),
]
