"""smarter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView

from repository.views import IndexView, DataSetListView, download
from accounts.views import UpdatedLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('login', UpdatedLoginView.as_view(), name="login"),
    path(
        'logout',
        LogoutView.as_view(template_name="accounts/logged_out.html"),
        name="logout"),
    path('datasets', DataSetListView.as_view(), name="dataset-list"),
    path('download/<path:file_name>', download, name='download'),
    path('', IndexView.as_view(), name="index"),
]
