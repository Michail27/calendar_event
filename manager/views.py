from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from manager.models import ProfileUser
from manager.serializers import RegisterSerializers, EventSerializers, LoginSerializers


class Register(GenericAPIView):
    serializer_class = RegisterSerializers

    def post(self, request):
        if not ProfileUser.objects.filter(username=request.data['username']):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"Your Userprofile is registered"}, status=status.HTTP_200_OK)
        return Response("this Userprofile already exist")


class Login(GenericAPIView):
    serializer_class = LoginSerializers

    def post(self, request):
        login = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = auth.authenticate(request, username=login, email=email, password=password)
        if user is not None:
            if email == ProfileUser.objects.filter(username=login)[0].email:
                token, flag = Token.objects.get_or_create(user=user)
                send_mail("It's your token for calendar_event", f"token: {token.__str__()}",
                          "michail27.03@gmail.com", [request.data["email"]], fail_silently=True)
                return Response("Your token to your e-mail")
            return Response('the mail is not correct')
        return Response("this Userprofile not exist")


class CreateEventSerializater(CreateAPIView):
    serializer_class = EventSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        event = EventSerializers(data=request.data)
        if event.is_valid():
            event.save(user_event=request.user)
        return Response({}, status=status.HTTP_201_CREATED)
