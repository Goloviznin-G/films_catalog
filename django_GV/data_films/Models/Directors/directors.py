from django.db import models


class Directors(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'directors'

    def __str__(self):
        return f'{self.name} {self.last_name}'