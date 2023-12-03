from django.db import models
from journeys.models import Journey
from users.models import User


class Order(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")


class Ticket(models.Model):
    cargo = models.IntegerField()
    seat = models.IntegerField()
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tickets")
