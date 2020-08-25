from django.db import models


class Notifications(models.Model):

    sent_date = models.DateTimeField()
