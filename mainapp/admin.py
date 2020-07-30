from django.contrib import admin
from .models import Group, SubgroupImage, Product, ProductImage



class SubgroupImageInline(admin.TabularInline):
    model = SubgroupImage
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = [SubgroupImageInline,]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]

admin.site.register(Group, GroupAdmin)
admin.site.register(Product, ProductAdmin)
