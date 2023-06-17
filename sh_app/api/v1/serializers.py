from rest_framework import serializers

from sh_app.models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = ('a', 'b')