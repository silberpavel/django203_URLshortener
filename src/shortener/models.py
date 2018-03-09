
from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = KirrURL.objects.filter(id__gte=1)  
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)



class KirrURL(models.Model):
    url         = models.CharField(max_length=220, )    # new field
    shortcode   = models.CharField(max_length=10, unique=True, blank=True) # unique=True => все shortcode must be unique
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