from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View   # for class based view

from analytics.models import ClickEvent

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
        context = {
            "title": "Kirr.co",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exist.html"
      
        return render(request, template, context)

 # class based view
class KirrURLRedirectView(View): 
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode=shortcode)
        # print(qs.first(), 'my test')
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        # print(ClickEvent.objects.create_event(obj))
        # print(obj.url)
        print('print')
        print(obj.url)
        return HttpResponseRedirect('https://www.yahoo.com/search/')












