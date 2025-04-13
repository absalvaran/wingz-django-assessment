from rest_framework import viewsets, permissions
from knox.auth import TokenAuthentication
from django.contrib.auth import get_user_model, login
from .serializers import UserSerializer, AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response

User = get_user_model()


class UserView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        email = user.email
        login(request, user)
        knox_response = super(LoginView, self).post(request, format=None)
        knox_response.data["email"] = email

        return Response(knox_response.data)
