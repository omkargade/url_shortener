from rest_framework import serializers
from .models import Shorted


class ShortedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shorted
        fields = ('url', 'short_url')
