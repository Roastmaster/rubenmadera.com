from __future__ import unicode_literals

from django.db import models

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to
from django.utils.translation import ugettext_lazy as _

# Create your models here.
#
#
# HOMEPAGE:
#

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="Put your name here or something")
    sub_heading = RichTextField(max_length=1000,
    	help_text="Maybe a brief description of who you are or something")
    avatar = FileField(verbose_name=_("Avatar"),
        help_text="A high res photo that will appear on the homepage",
        upload_to=upload_to("lens.uploaded.image", "PhotoEntries"),
        format="Image", max_length=255, null=True, blank=True)
    banner = FileField(verbose_name=_("Banner"),
        help_text="A high res photo that will appear on the homepage",
        upload_to=upload_to("lens.uploaded.image", "PhotoEntries"),
        format="Image", max_length=255, null=True, blank=True)
    copyright = RichTextField(max_length=1000)


    '''
    Section 2
    '''
    section_2_heading = models.CharField(max_length=200,
        help_text="Put your name here or something", default="about")
    section_2_sub_heading = RichTextField(max_length=1000,
        help_text="Maybe a brief description of who you are or something")
    section_2_blurb = RichTextField(max_length=1000,
            help_text="A brief blurb about this section.")

    '''
    Section 3
    '''

    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "Home pages"
