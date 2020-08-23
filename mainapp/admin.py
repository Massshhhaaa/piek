from django.contrib import admin
from .models import Group, Product, ProductImage, Modification



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]
    list_display = ('href_title', 'parent')

class ModificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug_mod')
    # exclude = ('slug_mod',)
    pass

admin.site.register(Group)
admin.site.register(Product, ProductAdmin)
admin.site.register(Modification, ModificationAdmin)
