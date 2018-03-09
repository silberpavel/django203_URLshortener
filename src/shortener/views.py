from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
    # print(args)
    # print(kwargs)
    # print(shortcode)
    return HttpResponse("Hello {sc}".format(sc=shortcode))


class HomeView(View):  # class based view
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

class KirrCBView(View): # class based view
    # def get(self, request, shortcode=None, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        # print(args)
        # print(kwargs)
        # print(shortcode)
        return HttpResponse("Hello again {sc}".format(sc=shortcode))
