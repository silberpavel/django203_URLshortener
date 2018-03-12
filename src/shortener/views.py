from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View   # for class based view

from forms import SubmitUrlForm
from .models import KirrURL  # Query the Database with the Shortcode

# fbv
def home_view_fbv(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST)
    return render(request, "shortener/home.html", {})

# class based view
class HomeView(View):  
    def get(self, request, shortcode=None, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Submit URL",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("url"))

        context = {
            "title": "Submit URL",
            "form": form
        }
        return render(request, "shortener/home.html", context)

 # class based view
class KirrCBView(View): 
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()












