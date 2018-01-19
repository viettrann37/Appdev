from django.contrib.auth.models import User, Group
from models import Company,Sneaker,Clothes
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, CompanySerializer, SneakerSerializer, ClothesSerializer 

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SneakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer

class ClothesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

