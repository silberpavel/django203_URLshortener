from django.conf.urls import url
from django.contrib import admin
# from django.urls import path

from shortener.views import KirrURLRedirectView, HomeView

# DO NOT DO
# from shortener import views
# from another_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', KirrURLRedirectView.as_view(), name='scode'),
]
