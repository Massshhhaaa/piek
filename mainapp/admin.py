from django.contrib import admin
from .models import Categories, Subgroup, SubgroupImage



class SubgroupImageInline(admin.TabularInline):
    model = SubgroupImage
    extra = 1

class SubgroupAdmin(admin.ModelAdmin):
    inlines = [SubgroupImageInline,]

admin.site.register(Categories)
admin.site.register(Subgroup, SubgroupAdmin)
