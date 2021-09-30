"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from .settings import DEBUG
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("api/v1/", include("apps.contacts.urls", namespace="contacts")),
    path("api/v1/super-login/", obtain_jwt_token, name="super_login"),
]

if DEBUG:
    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
