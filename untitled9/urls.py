"""untitled9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from close.views import TwitterLogin, HomeView, home_timeline, usercredential, mention, TwitterConnect,follower

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/twitter1/$', TwitterLogin.as_view(), name='twitter_login'),
    url(r'^rest-auth/home1/$', HomeView.as_view(), name='home_view'),
    url(r'^rest-auth/home2/$', home_timeline.as_view(), name='home_view'),
    url(r'^rest-auth/home3/$', usercredential.as_view(), name='home_view'),
    url(r'^rest-auth/home4/$', mention.as_view(), name='home_view'),
    url(r'^rest-auth/twitter/connect/$', TwitterConnect.as_view(), name='twitter_connect'),
    url(r'^rest-auth/home5/$', follower.as_view(), name='home_view'),


]
