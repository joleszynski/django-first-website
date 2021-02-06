from django.shortcuts import render
from team.models import Group
from .models import Day


def graphic(request):
    groups = Group.objects.all()
    day = Day.objects.all()
    days = []
    for i in day:
        days.append(i.week_day.all())
    context = {'days': days, 'groups': groups}

    return render(request, "graphic/graphic.html", context)
