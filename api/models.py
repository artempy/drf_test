from django.db import models


class App(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=32, db_index=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return '{} '.format(self.name)
