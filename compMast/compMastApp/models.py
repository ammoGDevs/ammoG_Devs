from django.db import models

class UserInput(models.Model):
    text = models.TextField()

    class Meta:
        app_label = 'compMastApp'

