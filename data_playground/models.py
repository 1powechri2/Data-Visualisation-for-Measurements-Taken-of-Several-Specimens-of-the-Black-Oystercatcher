from django.db import models

class BlackOystercatcher(models.Model):
    bird_id = models.CharField(max_length = 100)
    bird_location = models.CharField(max_length = 200)
    general_location = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sex = models.CharField(max_length = 100)
    date = models.DateTimeField()
    tarsus_length = models.FloatField()
    body_length = models.FloatField()
    head_length = models.FloatField()
    head_width = models.FloatField()
    head_height = models.FloatField()
    culmen_length = models.FloatField()
    culmen_height = models.FloatField()
    culmen_width = models.FloatField()
    bill_tip_height = models.FloatField()
    bill_1cm_height = models.FloatField()
    bill_2cm_height = models.FloatField()
    bill_3cm_height = models.FloatField()
    bill_4cm_height = models.FloatField()
    bill_tip_width = models.FloatField()
    bill_1cm_width = models.FloatField()
    bill_2cm_width = models.FloatField()
    bill_3cm_width = models.FloatField()
    bill_4cm_width = models.FloatField()

    def __str__(self):
        return self.bird_id
