from django.contrib import admin

# Register your models here.
from .models import New, Dino, Book, Autor, Cat, Order, SubOrder

#class OrganizationAdmin(admin.ModelAdmin):
#    list_display = ['name', 'region', 'in_msk', 'flag']

admin.site.register(New)
admin.site.register(Dino)
admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Cat)
admin.site.register(Order)
admin.site.register(SubOrder)