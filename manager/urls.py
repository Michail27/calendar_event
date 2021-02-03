from django.urls import path
from manager.views import Register, CreateEventSerializater, Login, UserHolidays, UserEvent

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path("createevent/", CreateEventSerializater.as_view(), name='create-event'),
    path('listholidays/', UserHolidays.as_view(), name='list-holidays'),
    path('listevent/<str:data>/', UserEvent.as_view(), name='list-event'),
]