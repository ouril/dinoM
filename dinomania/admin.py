from django.contrib import admin

# Register your models here.
from .models import New, Dino

#class OrganizationAdmin(admin.ModelAdmin):
#    list_display = ['name', 'region', 'in_msk', 'flag']

admin.site.register(New)
admin.site.register(Dino)
