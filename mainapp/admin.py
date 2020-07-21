from django.contrib import admin
from .models import Categories, Subgroup, Image



class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class CategoriesAdmin(admin.ModelAdmin):
    form = CategoriesForm
    inlines = [ImageInline]

    def save_model(self, request, obj, form, change):
        super(CategoriesAdmin,self).save_model(request, obj, form, change)
        # obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.images.create(file=afile)


@admin.register(Categories)
class PostAdmin()
