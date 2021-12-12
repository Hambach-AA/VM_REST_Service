from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from Inventory.models import ItemType


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
          model = ItemType
          fields = ['id', 'name']
