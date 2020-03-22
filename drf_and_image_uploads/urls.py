from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings

from drf_and_image_uploads.apps.accounts.views import UserAvatarUpload
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/auth-token/", obtain_auth_token, name="rest_auth_token"),
    path("api/user-avatar/", UserAvatarUpload.as_view(), name="rest_user_avatar_upload"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
