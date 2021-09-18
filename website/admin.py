from django.contrib import admin
from . import models
from django.conf import settings

class Module_Admin(admin.ModelAdmin):
    list_display = ('module_numbering' , 'module_numbering_title' , 'module_subtitle_numbering' ,'module_numbering_subtitle')
    list_filter = ('module_numbering_title' ,)
    search_fields = ('module_numbering_title' ,'module_numbering_subtitle',)
    list_per_page = 20


admin.site.register(models.Module,Module_Admin)