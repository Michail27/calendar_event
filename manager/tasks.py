import pytz
from django.core.mail import send_mail
from manager.models import CreateEvent
from datetime import datetime


def check_send_email():
    now_time = pytz.UTC.localize(datetime.now())
    events = CreateEvent.objects.all()
    for event in events:
        if event.notification:
            if event.date_start - event.reminder < now_time:
                email = event.user_event.email
                send_mail("It's your Planned event",
                          f"Event:{event.title}, Time:{event.date_start}",
                          "michail27.03@gmail.com", [email])
                event.notification = False
                event.save()
                return 'Dane'
