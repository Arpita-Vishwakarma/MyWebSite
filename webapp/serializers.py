# serializers.py
from rest_framework import serializers

class UserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(style={'base_template': 'textarea.html'})
