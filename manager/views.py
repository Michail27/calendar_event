from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView
from manager.serializers import RegisterSerializers, UserSerialisers, EventSerializers


class Register(GenericAPIView):
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'user': UserSerialisers(user, context=self.get_serializer_context()).data, },
                        status=status.HTTP_201_CREATED)


class CreateEventSerializater(CreateAPIView):
    serializer_class = EventSerializers

    def create(self, request):
        event = EventSerializers(data=request.data)
        if event.is_valid():
            event.save(user_event=request.user)
        return Response({}, status=status.HTTP_201_CREATED)
