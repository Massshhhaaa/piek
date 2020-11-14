from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from mainapp.models import Group

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['about']

    def location(self, item):

        return reverse(item)


class GroupsSitemap(Sitemap):

    def items(self):
        return Group.objects.all()
