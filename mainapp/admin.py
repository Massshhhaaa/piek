from django.contrib import admin
from .models import Group, Product, ProductImage, Modification, ProductDocs, Documentation
from django.utils.translation import ugettext_lazy as _

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    classes = ('grp-collapse grp-open',)


class ModificationInline(admin.StackedInline):
    exclude = ('slug_mod',)
    model = Modification
    extra = 0

class ProductDocsInline(admin.StackedInline):
    model = ProductDocs
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('parent',)
    inlines = [ProductImageInline, ModificationInline, ProductDocsInline]
    list_display = ('href_title', 'parent', 'slug_product',)

class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name' , 'key_filter', 'key_sort')

class ModificationAdmin(admin.ModelAdmin):
    exclude = ('slug_mod',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Group)
admin.site.register(Documentation, DocumentationAdmin)
