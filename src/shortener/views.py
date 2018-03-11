from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View   # for class based view

from .models import KirrURL  # Query the Database with the Shortcode


# fbv
def home_view_fbv(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST)
    return render(request, "shortener/home.html", {})

# class based view
class HomeView(View):  
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        # some_dict = {}
        # some_dict['url']  # error
        # some_dict.get('url', 'http://www.cnn.com/')  # none
        # print(request.POST)
        # print(request.POST["url"])
        # print(request.POST.get("url"))
        return render(request, "shortener/home.html", {})

 # class based view
class KirrCBView(View): 
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()












