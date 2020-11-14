from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from mainapp.models import Group, Product, Modification

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['main_def','about', 'docs']

    def location(self, item):
        return reverse(item)


class GroupsSitemap(Sitemap):
    def items(self):
        return Group.objects.all()


class ProductsSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

class ModificationsSitemap(Sitemap):
    def items(self):
        return Modification.objects.all()
