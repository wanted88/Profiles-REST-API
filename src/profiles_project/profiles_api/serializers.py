from rest_framework import serializers


class HelloSerializer(serializers.Serializers):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)
