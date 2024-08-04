from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','date')
    prepopulated_fields={'slug':('title',)}

class PostContact(admin.ModelAdmin):
    list_display=('name','mail','message')

admin.site.register(models.Author)
admin.site.register(models.Tag)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Contact,PostContact)
