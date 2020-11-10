from rest_framework import serializers
from app.models import LogMessage

class LogMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogMessage
        fields = ('id', 'message', 'log_date')

