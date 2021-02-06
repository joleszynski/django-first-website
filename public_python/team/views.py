from django.shortcuts import render

from .models import Trainer, Group, TeamDescribe


def team_list(request):
    trainers = Trainer.objects.all()
    groups = Group.objects.all()
    describe = TeamDescribe.objects.get(is_active=True)
    context = {
        "trainers": trainers,
        "groups": groups,
        "describe": describe,
    }
    return render(request, "team/team_list.html", context)
