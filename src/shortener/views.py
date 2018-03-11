from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View   # for class based view

from .models import KirrURL  # Query the Database with the Shortcode

def test_view(request):
    return HttpResponse("some stuff")


# function based view FBV
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # do something
    return HttpResponseRedirect(obj.url)


 # class based view
class KirrCBView(View): 
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()


# class based view
class HomeView(View):  

    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})










