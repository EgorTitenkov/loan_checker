from rest_framework import serializers

from MyAPI.models import Approvals


class ApprovalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approvals,
        fields = '__all__'






