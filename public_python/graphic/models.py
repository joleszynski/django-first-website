from django.db import models
from team.models import Group


class Day(models.Model):
    DAYS = [
        ("Poniedziałek", "Poniedziałek"),
        ("Wtorek", "Wtorek"),
        ("Środa", "Środa"),
        ("Czwartek", "Czwartek"),
        ("Piątek", "Piątek")
    ]
    day = models.CharField(
        max_length=13, choices=DAYS, default="Poniedziałek")

    def __str__(self):
        return self.day


class IndexDay(models.Model):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="week_day")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="group")
    place = models.CharField(max_length=100, default='')
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return self.group.name
