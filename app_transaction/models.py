from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)
    #owner = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name

class Member(models.Model):
    group = models.ForeignKey( Group, on_delete=models.CASCADE, \
            related_name="kelompok_group")
    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=200)
    #addres2 = models.CharField(max_length=200)
    #addresz = models.CharField(max_length=100)
    ethnic = models.CharField(max_length=100, default=None)

    class Meta:
        indexes = [
            models.Index(fields=['address', 'name']),
            models.Index(fields=['ethnic'], name='ethnic_index'),
        ]
        unique_together = (('name','address'),('address','ethnic'))

    def __str__(self):
        return self.name
