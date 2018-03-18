from django.conf import settings    # for static files
from django.db import models

# from django.core.urlresolvers import reverse
from django.urls import reverse
from django_hosts.resolvers import reverse

# Create your models here.
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

# static files value set, if is not it will set default
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)  
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.url)    # q.id
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)



class KirrURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])    # new field
    # unique=True => все shortcode must be unique
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    #shortcode = models.CharField(max_length=25, unique=True, default='http://www.gugul.com/')

    updated     = models.DateTimeField(auto_now=True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add=True) # when model was created
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False) # date that we can set
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)  # .save()

    def __str__(self):
        return str(self.url)            # returns the model's url
  
    def __unicode__(self):
        return str(self.url) 

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http', port='8000')
        return url_path
