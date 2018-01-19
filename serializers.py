from django.contrib.auth.models import User, Group
from models import Company,Sneaker,Clothes
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('url', 'name', 'address')

class SneakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sneaker
        fields = ('url', 'brand', 'color')

class ClothesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothes
        fields = ('url', 'brand', 'size')

