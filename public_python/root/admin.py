from django.contrib import admin
from .models import HomeDescribe, Contact, PricingPlan, Activity, AgreementFiles, PrivacyPolicy


admin.site.register(HomeDescribe)
admin.site.register(Contact)
admin.site.register(AgreementFiles)
admin.site.register(PrivacyPolicy)

class ActivityInline(admin.TabularInline):
    model = Activity


class PricingAdmin(admin.ModelAdmin):
    inlines = [
        ActivityInline,
    ]


admin.site.register(PricingPlan, PricingAdmin)
