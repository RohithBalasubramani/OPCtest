from django.contrib import admin
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from django.utils.formats import localize
from django.utils.timezone import localtime

# Get all models from your app
app_models = apps.get_app_config('opc_app').get_models()

# Custom admin class to dynamically display all fields and include import-export functionality
class DynamicFieldsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        # Dynamically set the list_display attribute
        self.list_display = [field.name for field in model._meta.fields]
        # Set ordering by 'timestamp' if it exists
        if 'timestamp' in self.list_display:
            self.ordering = ['-timestamp']
        super().__init__(model, admin_site)
    
    def formatted_timestamp(self, obj):
        # Ensure the timestamp is localized and displayed with seconds
        return localize(localtime(obj.timestamp), use_l10n=True)
    formatted_timestamp.short_description = 'Timestamp'

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if 'timestamp' in list_display:
            list_display = tuple(field if field != 'timestamp' else 'formatted_timestamp' for field in list_display)
        return list_display

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'timestamp':
            formfield.widget.format = '%Y-%m-%d %H:%M:%S'
            formfield.widget.attrs['class'] = 'vDateTimeField'
        return formfield

# Register all models with the custom admin class
for model in app_models:
    admin.site.register(model, DynamicFieldsAdmin)
