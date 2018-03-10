from django.http import HttpResponse
from django.shortcuts import render
from django.views import View   # for class based view

# Create your views here.

# function based view FBV
def kirr_redirect_view(request, *args, **kwargs):  
    return HttpResponse("Hello")


# class based view
class HomeView(View):  

    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})


 # class based view
class KirrCBView(View):    
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello again")
