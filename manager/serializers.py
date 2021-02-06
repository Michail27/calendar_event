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




class HolidausSerializers(ModelSerializer):
    class Meta:
        model = Holidays
        fields = ('title', 'holiday_start', 'holiday_finish')


class ListEventSerializers(ModelSerializer):
    class Meta:
        model = CreateEvent
        fields = ['title', "date_start"]
