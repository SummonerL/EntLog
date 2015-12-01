from django.contrib import admin
from .models import Entry

# Here are the classes that configure the admin view for our models
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name','ent_type', 'completion_date', 'entry_updated',)

# Register your models here - tells the admin that these objects have admin interface
admin.site.register(Entry, EntryAdmin)
