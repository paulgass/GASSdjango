from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
