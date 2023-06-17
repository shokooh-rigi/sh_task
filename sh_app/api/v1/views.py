from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from .serializers import CalculationSerializer
from ...models import Calculation


class CustomThrottle(UserRateThrottle):
    rate = '100/hour'


@throttle_classes([CustomThrottle])
class SumAPIView(APIView):
    def get(self, request, format=None):
        a = int(request.GET.get('a', 0))
        b = int(request.GET.get('b', 0))
        result = a + b
        return Response({'result': result})


class HistoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


class TotalAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        total = Calculation.objects.aggregate(Sum('a'), Sum('b'))
        total = sum(total.values())
        return Response({'total': total})
