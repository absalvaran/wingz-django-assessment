from rest_framework import viewsets
from knox.auth import TokenAuthentication
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


class UserViews(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
