from django.db import models
from pytils.translit import slugify
from tinymce import HTMLField

# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(null=True, blank=True,max_length=250)
    img = models.ImageField(upload_to='main_page', null=True, blank=True)
    slug = models.CharField('url', unique=True, null=True, blank=True, max_length=200, help_text='for instance, "mechanisms/meo"' )
    description = models.TextField(max_length=500, null=True, blank=True)
    content = HTMLField(null=True, blank=True, )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.title)

class SubgroupImage(models.Model):
    page = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mechanisms', null=True)

    def __str__(self):
        return str(self.page)



class Product(models.Model):
    parent = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug_product = models.SlugField('url', help_text='for instance, "40 or 6_3"')
    img = models.ImageField('Изображение для ссылки', null=True, blank=True, upload_to='mechanisms_preview')
    href_title = models.CharField('Имя ссылки', max_length=250)
    name = models.CharField('Имя группы', max_length=250)
    description = HTMLField()
    content = HTMLField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.href_title)

class ProductImage(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mechanisms', null=True)

    def __str__(self):
        return str(self.page.name)
