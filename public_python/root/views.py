import json

from django.shortcuts import render
from django.http import FileResponse, Http404, JsonResponse
from django.core import serializers

from blog.models import BlogPost
from .models import HomeDescribe, Contact, PricingPlan, AgreementFiles, PrivacyPolicy

# View of MainSite


def home(request):
    body_head = HomeDescribe.objects.get(is_active=True)
    blog_index = BlogPost.objects.order_by('-pub_date')[:5]
    context = {
        "body_head": body_head,
        "blog_index": blog_index,
    }
    return render(request, "root/home.html", context)

# View of Contact site


def contact(request):
    contacts = Contact.objects.all()
    return render(request, "root/contact.html", {"contact": contacts})


def pricing(request):
    plan = PricingPlan.objects.get(is_active=True)
    activity_row = plan.activity.all()
    files = AgreementFiles.objects.get(is_active=True)
    file_rule = files.rule_name
    file_agreement = files.agreement_name
    context = {"plan": plan, "activity": activity_row,
               "file_rule": file_rule, "file_agreement": file_agreement}
    return render(request, "root/pricing.html", context)


def pdf(request, file_name):
    try:
        return FileResponse(open('public/media/documents/' + file_name, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


# API for reload posts on home
def posts_onload(request):
    blog_json = serializers.serialize(
        'json', BlogPost.objects.order_by('-pub_date')[:5])
    return JsonResponse(blog_json, safe=False)


def posts_reload(request):
    data = json.loads(request.body.decode("utf-8"))
    len_list = data['postsLen']
    to_list = len_list + 5
    blog_index = BlogPost.objects.order_by('-pub_date')[len_list:to_list]
    serial_data = serializers.serialize(
        'json', blog_index)

    return JsonResponse(serial_data, safe=False)


def privacy_policy(request):
    document = PrivacyPolicy.objects.get(is_active=True)
    return render(request, 'root/privacy_policy.html', {"document": document})