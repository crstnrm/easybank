from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.short_name

    @property
    def rate(self):
        now = timezone.now()
        if self.short_name == 'SQUA':
            return now.month / now.year
        if self.short_name == 'SCO':
            return now.day * 0.5
        if self.short_name == 'PERE':
            return now.month * 0.1


class Card(models.Model):
    number = models.IntegerField(unique=True)
    cardholder = models.ForeignKey('cards.Person', on_delete=models.CASCADE)
    limit = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    expires = models.DateTimeField()
    brand = models.ForeignKey('cards.Brand', on_delete=models.PROTECT)


class Person(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dni = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.dni


class Operation(models.Model):
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
