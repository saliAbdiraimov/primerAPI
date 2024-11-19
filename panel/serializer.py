
from rest_framework import serializers

from .models import panel


class panelSerializer(serializers.ModelSerializer):
    class Meta:
        model = panel
        fields = '__all__'
