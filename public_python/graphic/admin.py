from django.contrib import admin
from .models import Day, IndexDay


class IndexDayInline(admin.TabularInline):
    model = IndexDay


class DayAdmin(admin.ModelAdmin):
    inlines = [
        IndexDayInline,
    ]


admin.site.register(Day, DayAdmin)
