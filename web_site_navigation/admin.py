from django.contrib import admin


# Register your models here.

from .models import web_class,web_site,web_class_obj


class web_class_objInline(admin.StackedInline):
    model = web_class_obj

class web_classAdmin(admin.ModelAdmin):
    inlines = [web_class_objInline,]
    list_display = ['class_name', 'ctime','uptime']
    list_filter = ['class_name']
    search_fields = ['class_name']
    list_per_page = 10



class web_siteInline(admin.StackedInline):
    model = web_site

class web_class_objAdmin(admin.ModelAdmin):
    inlines = [web_siteInline,]
    list_display = ['obj_name','obj_environment','web_class_id', 'ctime','uptime']
    list_filter = ['obj_name']
    search_fields = ['obj_name']
    list_per_page = 10



class web_siteAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'site_url','web_class_obj_id','ctime','uptime']
    list_filter = ['site_name']
    search_fields = ['site_name']
    list_per_page = 10


admin.site.register(web_class,web_classAdmin)
admin.site.register(web_class_obj,web_class_objAdmin)
admin.site.register(web_site,web_siteAdmin)

