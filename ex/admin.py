from django.contrib import admin
from .models import star
from django.utils.safestring import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.


class Displaystar(ImportExportMixin, admin.ModelAdmin):
    list_display = ('get_image', 'name', 'job', 'birth', 'level', 'debut', )
    search_fields = ('name', 'job',)
    list_filter = ('job',)
    
    # list_editable = ('name', 'department',)
    def has_add_permission(self, request):
	    return False

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height ="{height}"/>'.format(
            url = obj.photo.url,
            width = 100,
            height = 100,
        ))


admin.site.register(star, Displaystar)
