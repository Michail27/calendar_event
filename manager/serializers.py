
from rest_framework.serializers import ModelSerializer
from manager.models import ProfileUser, CreateEvent


class UserSerialisers(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('id', 'username', 'email', 'country')


class RegisterSerializers(ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('id', 'username', 'email', 'password', 'country')
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_date):
        user = ProfileUser.objects.create_user(validated_date['username'],
                                               email=validated_date['email'],
                                               password=validated_date['password'],
                                               country=validated_date['country'],)
        return user


class EventSerializers(ModelSerializer):
    class Meta:
        model = CreateEvent
        fields = (
            "title",
            "date_start",
            "date_finish",
            "reminder",
        )
