from django.db import models


class DinAction(models.Model):
    action_text = models.CharField(max_length=500)