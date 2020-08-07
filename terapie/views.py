from django.shortcuts import render
from rest_framework import viewsets
from .models import Therapy
from .serializers import TherapySerializer,UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    def get_permissions(self):
        if self.action =='create':
            permission_classes=[AllowAny]
        else:
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]


class TherapyViewSet(viewsets.ModelViewSet):
    queryset =Therapy.objects.all()
    serializer_class = TherapySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    print('user')

