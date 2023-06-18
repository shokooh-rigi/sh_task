from django.conf import settings
from rest_framework.decorators import throttle_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from .serializers import CalculationSerializer
from ...models import Calculation


class CustomThrottle(UserRateThrottle):
    rate = settings.USER_RATE


@throttle_classes([CustomThrottle])
class SumAPIView(APIView):
    def get(self, request):
        a = int(request.GET.get('a', 0))
        b = int(request.GET.get('b', 0))
        result = a + b
        return Response({'result': result})


class HistoryViewSet(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


class TotalAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total = Calculation.objects.sum_all()
        return Response({'total': total})
