from rest_framework import serializers

from .models import approvals


class ApprovalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = approvals,
        fields = '__all__'






