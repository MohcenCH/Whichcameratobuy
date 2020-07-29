from django.contrib import admin
from .models import *
#from import_export.admin import ImportExportModelAdmin


admin.site.register(Product)
 
#@admin.register(Product)
#class ProductAdmin(ImportExportModelAdmin):
#    list_display = ("Price", "Color", "Continuous Shooting Speed", "Continuous_shooting","Screen Size","Focus Type","ISO Range","Item Dimensions","Item Weight"
#    , "Max Resolution" , "Optical Sensor Resolution" , "Optical Zoom","Photo Sensor Size","Video Capture Resolution","Viewfinder Type","Wireless Communication Technology","")
#    pass