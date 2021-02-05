from datetime import timedelta
from json import dumps
from django.test import TestCase
from requests import get
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, RequestsClient

from manager.models import ProfileUser


class RestTest(TestCase):
    def setUp(self):
        self.login = "test_name"
        self.email = 'test@test.tu'
        self.password = "useruser"
        self.user = ProfileUser.objects.create_user(
            username=self.login,
            email=self.email,
            password=self.password,
        )

    def test_add_event(self):
            url = reverse("login")
            data = {
                "username": self.login,
                "email": self.email,
                "password": self.password
            }
            response = self.client.post(
                path=url,
                data=dumps(data),
                content_type="application/json"
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            clint = RequestsClient()
            data = {
                "title": "Abdfghjglkf11",
                "date_start": "2021-02-01T07:25:00Z",
                "date_finish": "2021-02-01T10:25:00Z",
                "reminder": timedelta(seconds=7200),
                "notification": True}
            headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
            response = clint.get('http://127.0.0.1:8000/event/createevent/', headers=headers)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            response = clint.get('http://127.0.0.1:8000/event/createevent/', headers=headers, data=data)

    def test_register(self):
        url = reverse('register')
        data = {
            "username": 'test_name',
            "email": 'asdafd@fsg.dfv',
            "password": 'useruser',
            'country': 'Russia'
        }
        response = self.client.post(
            path=url,
            data=dumps(data),
            content_type="application/json"
        )
        self.assertNotEqual(response, status.HTTP_200_OK)

    def test_list_event(self):
            url = reverse("login")
            data = {
                "username": self.login,
                "email": self.email,
                "password": self.password
            }
            response = self.client.post(
                path=url,
                data=dumps(data),
                content_type="application/json"
            )
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            clint = RequestsClient()
            data = {
                "title": "Abdfghjglkf11",
                "date_start": "2021-02-01T07:25:00Z",
                "date_finish": "2021-02-01T10:25:00Z",
                "reminder": timedelta(seconds=7200),
                "notification": True}
            headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
            response = clint.get('http://127.0.0.1:8000/event/createevent/', headers=headers, data=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
            response = clint.get('http://127.0.0.1:8000/event/listevent/2021', headers=headers)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
            response = clint.get('http://127.0.0.1:8000/event/listevent/2021-02', headers=headers)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            response = clint.get('http://127.0.0.1:8000/event/listevent/2021-02-01', headers=headers)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
