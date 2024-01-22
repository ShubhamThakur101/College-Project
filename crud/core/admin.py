from django.contrib import admin

from .models import Table_details 
# Register your models here.

@admin.register(Table_details)
class Table_detailsAdmin(admin.ModelAdmin):
    list_display=['id','day','time','subject','tname','sclass','dname']

