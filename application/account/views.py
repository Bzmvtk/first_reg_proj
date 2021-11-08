from rest_framework import generics, status

from django.contrib.auth import get_user_model
from rest_framework.response import Response

from rest_framework.views import APIView

from application.account.serializers import RegisterSerializer

User = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Absolutely fuck', status=status.HTTP_200_OK)