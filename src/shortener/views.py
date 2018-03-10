from django.http import HttpResponse
from django.shortcuts import render
from django.views import View   # for class based view

# Create your views here.

# function based view FBV
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  
    # shortcode=None -> Error not accours
    # print(request.user)
    # print(request.user.is_authenticated())
    print(args)
    print(kwargs)   # -> {'slug': '123gg'}  http://127.0.0.1:8000/a/123gg/
    print(shortcode)
    return HttpResponse("Hello {sc}".format(sc=shortcode))


# class based view
class HomeView(View):  

    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

    def post(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})


 # class based view
class KirrCBView(View): 
    def get(self, request, shortcode=None, *args, **kwargs):
        print(args)
        print(kwargs)
        print(shortcode)
        return HttpResponse("Hello again {sc}".format(sc=shortcode))
