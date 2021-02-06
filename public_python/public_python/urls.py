from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("root.urls", namespace="root")),
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),
    path("o-nas/", include(("team.urls", "team"), namespace="team")),
    path("grafik/", include(("graphic.urls", "graphic"), namespace="graphic")),
]
#

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
