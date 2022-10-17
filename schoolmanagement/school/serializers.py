from rest_framework import serializers
from .models import MGender, TPersonData, MBloodGroup


class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonData
        fields = "__all__"


class BloodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MBloodGroup
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MGender
        fields = "__all__"
