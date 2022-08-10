from django.utils import timezone
from statistics import mode
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'brand'


class Model(models.Model):
    name = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        db_table = 'model'


class Vehicle(models.Model):
    STATUS = (
        ('available', 0),
        ('action_required', 1),
        ('action_in_progress', 2),
    )
    status = models.IntegerField(choices=STATUS)
    name = models.CharField(max_length=30)
    legal_identifier = models.CharField(max_length=30, unique=True)
    frame_size = models.IntegerField()

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now,)

    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = 'vehicle'
