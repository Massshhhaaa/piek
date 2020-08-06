from django.contrib import admin
from .models import Group, Product, ProductImage, Modification



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]

class ModificationAdmin(admin.ModelAdmin):
    exclude = ('slug_mod',)

admin.site.register(Group)
admin.site.register(Product, ProductAdmin)
admin.site.register(Modification, ModificationAdmin)
