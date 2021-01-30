from django.urls import path
from manager.views import Register, CreateEventSerializater, Login

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='register'),
    path("createevent/", CreateEventSerializater.as_view()),
]