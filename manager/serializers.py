from rest_framework.serializers import ModelSerializer
from manager.models import ProfileUser, CreateEvent, Holidays


class UserSerialisers(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('id', 'username', 'email', 'country')


class RegisterSerializers(ModelSerializer):
    class Meta:
        email = {'required': True}
        model = ProfileUser
        fields = ('id', 'username', 'email', 'password', 'country')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_date):
        user = ProfileUser.objects.create_user(validated_date['username'],
                                               email=validated_date['email'],
                                               password=validated_date['password'],
                                               country=validated_date['country'],)
        return user


class LoginSerializers(ModelSerializer):
    class Meta:
        model = ProfileUser
        email = {'required': True}
        fields = ['username', 'email', 'password']


class EventSerializers(ModelSerializer):
    class Meta:
        model = CreateEvent
        fields = ("title", "date_start", "date_finish", "reminder", 'notification')

# Для создания событий
# from requests import post
# from datetime import timedelta
# headers = {'Authorization': "Token 11ef02830a895cd2b190d8d814d56ad86cd5c5b4"}
# data = {
#     "title": "Abdfghjglkf11",
#     "date_start": "2021-02-01T07:25:00Z",
#     "date_finish": "2021-02-01T10:25:00Z",
#     "reminder": timedelta(seconds=7200),
#     "notification": True
# }
# response = post('http://127.0.0.1:8000/event/createevent/', headers=headers, data=data)


# для списка событий
# from requests import post, get
# headers = {'Authorization': "Token 03fe7b58b8ff9a2c2226ea5d2cf0ea3725dae2d6"}
# data = {
#     'search': '2021-03'
# }
# response = get('http://127.0.0.1:8000/event/listholidays/?search=2021-03', headers=headers, params=data)
# response.json()


class HolidausSerializers(ModelSerializer):
    class Meta:
        model = Holidays
        fields = ('title', 'holiday_start', 'holiday_finish')


class ListEventSerializers(ModelSerializer):
    class Meta:
        model = CreateEvent
        fields = ['title', "date_start"]
