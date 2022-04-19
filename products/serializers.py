from dataclasses import fields
from rest_framework import serializers
from .models import TablaItems

class TablaItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaItems
        fields= '__all__'