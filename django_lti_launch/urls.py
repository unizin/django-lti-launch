"""django_lti_launch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django_lti_launch.views import SuccessView
from ltilaunch.views import ReturnRedirectView, LaunchView, DevLoginView

urlpatterns = [
    url(r'^ltilaunch/', include('ltilaunch.urls')),
    url(r'^return', ReturnRedirectView.as_view(), name='return'),
    url(r'^admin/', admin.site.urls),
    url(r'^devlogin', DevLoginView.as_view(tool_provider_url='/tool')),
    url(r'^launch', LaunchView.as_view(tool_provider_url='/tool')),
    url(r'^tool', SuccessView.as_view())
]
