from django.contrib import admin

# Register your models here.
from .models import New, Dino, Book, Autor

#class OrganizationAdmin(admin.ModelAdmin):
#    list_display = ['name', 'region', 'in_msk', 'flag']

admin.site.register(New)
admin.site.register(Dino)
admin.site.register(Book)
admin.site.register(Autor)