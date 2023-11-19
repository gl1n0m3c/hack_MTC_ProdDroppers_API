from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users_auth.urls")),
    path("api-token-auth", views.obtain_auth_token),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
