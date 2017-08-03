from django.contrib import admin

# Register your models here.
from .models import New, Dino, Book, Autor, Order, SubOrder, Comment, Profile

#class OrganizationAdmin(admin.ModelAdmin):
#    list_display = ['name', 'region', 'in_msk', 'flag']

admin.site.register(New)
admin.site.register(Dino)
admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(SubOrder)
admin.site.register(Profile)