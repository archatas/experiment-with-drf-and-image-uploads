"""drf_and_image_uploads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings

from drf_and_image_uploads.apps.accounts.views import UserAvatarUpload
from rest_framework.authtoken import views


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path(
        "api/user-avatar/", UserAvatarUpload.as_view(), name="rest_user_avatar_upload"
    ),
    path("api/auth-token/", views.obtain_auth_token),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)
