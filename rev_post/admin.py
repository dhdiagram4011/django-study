from django.contrib import admin

from .models import *

class rev_postOption(admin.ModelAdmin):
    list_display = ['id','email','published_date','created_date']

admin.site.register(rev_post,rev_postOption)



