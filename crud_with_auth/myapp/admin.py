from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmim(admin.ModelAdmin):
    list_display = ['id','user','name','image','locality','city','zipcode','state']

