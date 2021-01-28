from django.urls import path
from manager.views import Register, CreateEventSerializater

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    path("createevent/", CreateEventSerializater.as_view()),
    # path('', MyPage.as_view(), name='the-main-page'),
]