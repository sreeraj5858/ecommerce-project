from django.contrib import admin

# Register your models here.
from .models import Category,Product
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated',]
    prepopulated_fields =  {'slug':('name',)}
    list_editable = ['price','stock','available',]
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

#
# from django.contrib import admin
# from .models import Category, Product
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
#     prepopulated_fields = {'slug': ('name',)}
#     list_editable = ['price', 'stock', 'available']
#     list_per_page = 20
#
#
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
