from django.db import models


class Vehicle(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    number_wheels = models.IntegerField()

    def __str__(self):
        # Display the name when this object is listed in the Django Admin page
        return self.name

    class Meta:
        db_table = 'vehicles'
