from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("kontakt/", views.contact, name="contact"),
    path("cennik/", views.pricing, name="pricing"),
    path("pdf/<str:file_name>", views.pdf, name="pdf"),
    path("posts-onload/", views.posts_onload, name="posts_onload"),
    path("posts-reload/", views.posts_reload, name="posts_reload"),
    path("polityka-prywatnosci/", views.privacy_policy, name="privacy_policy")
]
