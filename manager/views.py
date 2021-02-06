from django.contrib import auth
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView

from manager.models import ProfileUser, Holidays, CreateEvent
from manager.serializers import RegisterSerializers, EventSerializers, LoginSerializers, HolidausSerializers
from manager.serializers import ListEventSerializers


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
                          "ilya27.03.19888@gmail.com", [request.data["email"]])
                return Response("Your token to your e-mail", status=status.HTTP_200_OK)
            return Response('the mail is not correct')
        return Response("this Userprofile not exist")


class CreateEventSerializater(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializers
    queryset = CreateEvent.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_event=self.request.user)


class UserHolidays(ListAPIView):
    filter_backends = [SearchFilter]
    serializer_class = HolidausSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    search_fields = ['holiday_start']

    def get_queryset(self):
        holidays = Holidays.objects.filter(country=self.request.user.country_id)
        return holidays


class UserEvent(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, data):
        data = data.split("-")
        event = CreateEvent.objects.filter(user_event=request.user)
        if len(data) == 1:
            event = event.filter(date_start__year=data[0])
        elif len(data) == 2:
            event = event.filter(date_start__year=data[0], date_start__month=data[1])
        elif len(data) == 3:
            event = event.filter(date_start__year=data[0],
                                 date_start__month=data[1],
                                 date_start__day=data[2])
        serializer = ListEventSerializers(event.order_by("date_start"), many=True)
        return Response(serializer.data)
