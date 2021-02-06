from django.db import models


# MainSite
class HomeDescribe(models.Model):
    name = models.CharField(max_length=255)
    describe = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ContactSite
class Contact(models.Model):
    phone_number = models.CharField(max_length=100, default="+48 606 606 606")
    email = models.EmailField(max_length=100)
    instagram = models.CharField(max_length=100)
    instagram_link = models.URLField(max_length=100, default='')
    facebook = models.CharField(max_length=100)
    facebook_link = models.URLField(max_length=100, default='')

    def __str__(self):
        return self.email


# PricingSite Models
class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    describe = models.TextField(blank=True, max_length=150)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Activity names on pricing site
class Activity(models.Model):
    plan = models.ForeignKey(
        PricingPlan, on_delete=models.CASCADE, related_name="activity"
    )
    activity_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

# Files model to download from pricing site
class AgreementFiles(models.Model):
    name = models.CharField(max_length=80, default="Pliki_Rok")
    rule = models.FileField(upload_to="documents/")
    rule_name = models.CharField(max_length=50, default="regulamin.pdf")
    agreement = models.FileField(upload_to="documents/")
    agreement_name = models.CharField(max_length=50, default="umowa.pdf")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Newly created object, so set slug
            self.rule_name = str(self.rule)
            self.agreement_name = str(self.agreement)

        super(AgreementFiles, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PrivacyPolicy(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
