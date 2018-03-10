from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View   # for class based view

from .models import KirrURL  # Query the Database with the Shortcode


# function based view FBV
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  
    print('method is \n')
    print(request.method)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponse("Hello {sc}".format(sc=obj.url))


 # class based view
class KirrCBView(View): 
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse("Hello again {sc}".format(sc=obj.url))

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()

# class based view
class HomeView(View):  

    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})
