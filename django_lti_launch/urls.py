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
from django.views.generic import TemplateView

from django_lti_launch.views import TestLaunchView
from ltilaunch.views import ReturnRedirectView

urlpatterns = [
    url(r'^ltilaunch/', include('ltilaunch.urls')),
    url(r'^return', ReturnRedirectView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^launch', TestLaunchView.as_view(
        tool_provider_url='return?lti_errormsg=Who%27s+going+to+save+you,+'
                          'Junior%3F!')),
    url(r'^succeeded', TemplateView.as_view(template_name='success.html'))
]
