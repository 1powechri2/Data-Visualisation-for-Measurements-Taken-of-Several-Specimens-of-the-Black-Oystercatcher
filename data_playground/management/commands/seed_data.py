from django.core.management.base import BaseCommand
import csv
import datetime
from data_playground.models import BlackOystercatcher

class Command(BaseCommand):

    def create_model(self):
        with open('data_playground/specimens.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                BlackOystercatcher(bird_id = row['Bird_ID'],
                                  bird_location = row['Bird_Location'],
                                  general_location = row['General_Location'],
                                  region = row['Region'],
                                  latitude = row['Latitude'],
                                  longitude = row['Longitude'],
                                  sex = row['Sex'],
                                  date = self.format_date(row['Date']),
                                  tarsus_length = row['Tarsus_length'],
                                  body_length = row['Body_length_cm'],
                                  head_length = row['Head_length'],
                                  head_width = row['Head_width'],
                                  head_height = row['Head_height'],
                                  culmen_length = row['Culmen_length'],
                                  culmen_height = row['Culmen_height'],
                                  culmen_width = row['Culmen_width'],
                                  bill_tip_height = row['Bill_tip_height'],
                                  bill_1cm_height = row['Bill_1cm_height'],
                                  bill_2cm_height = row['Bill_2cm_height'],
                                  bill_3cm_height = row['Bill_3cm_height'],
                                  bill_4cm_height = row['Bill_4cm_height'],
                                  bill_tip_width = row['Bill_tip_width'],
                                  bill_1cm_width = row['Bill_1cm_width'],
                                  bill_2cm_width = row['Bill_2cm_width'],
                                  bill_3cm_width = row['Bill_3cm_width'],
                                  bill_4cm_width = row['Bill_4cm_width']).save()

    def format_date(self, date):
        try:
            return datetime.datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            return datetime.datetime.strptime(date, "%Y")

    def handle(self, *args, **options):
        self.create_model()
