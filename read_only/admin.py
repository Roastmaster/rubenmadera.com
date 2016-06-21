from django.contrib import admin
from models import HomePage
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
# Register your models here.

class HomePageAdmin(PageAdmin):
	pass

admin.site.register(HomePage, HomePageAdmin)