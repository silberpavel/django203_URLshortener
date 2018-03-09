"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
#from django.urls import include, path
from shortener import views

from shortener.views import HomeView, kirr_redirect_view, KirrCBView

urlpatterns = [
    #path('', views.index, name='main-view'),
    path('', HomeView.as_view()),
    path(r'admin/', admin.site.urls),
    path(r'view-1/', kirr_redirect_view),   # 1.10 -> url(r'^view-1/$'
    path(r'view-2/', KirrCBView.as_view()),


    #path(r'\^a/[0-9]\*/', kirr_redirect_view),
    #path(r'b/\^(?P<slug>[\w-]\+)/\$', KirrCBView.as_view()),
]
