from django.urls import path
from . import views


urlpatterns = [
    path("<slug:post_slug>", views.post_detail, name="post_detail"),
]
