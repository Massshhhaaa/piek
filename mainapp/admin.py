from django.contrib import admin
from .models import Categories, Subgroup, SubgroupImage, Product, ProductImage



class SubgroupImageInline(admin.TabularInline):
    model = SubgroupImage
    extra = 1

class SubgroupAdmin(admin.ModelAdmin):
    inlines = [SubgroupImageInline,]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]

admin.site.register(Categories)
admin.site.register(Subgroup, SubgroupAdmin)
admin.site.register(Product, ProductAdmin)
