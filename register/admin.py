from django.contrib import admin

from .models import *

class AgreementOption(admin.ModelAdmin):
    list_display = ['all_consent','membership_terms','check_01','privacy','check_02','overseas_transfer','check_03','three_party','check_04','marketing','check_05']

admin.site.register(Agreement,AgreementOption)