from django.urls import path, include
from rest_framework import routers

from .views import HistoryViewSet, SumAPIView, TotalAPIView

app_name = 'sh_app'

router = routers.DefaultRouter()
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('sum/', SumAPIView.as_view()),
    path('total/', TotalAPIView.as_view()),
    path('', include(router.urls)),

]

urlpatterns += router.urls
