from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from manager.models import Country
from requests import get


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://www.officeholidays.com/countries"
        script_defer = BeautifulSoup(get(url).text)
        for teg_li in script_defer.find_all("div", {"class": "four omega columns"}):
            for country in teg_li.find_all("a"):
                country = country.text[2:]
                Country.objects.create(country=country)
