from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Course)
admin.site.register(Application)
admin.site.register(Result)
admin.site.register(LandingPageData)