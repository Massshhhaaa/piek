from django.db import models
from pytils.translit import slugify
from tinymce import HTMLField
from django.shortcuts import reverse

class Group(models.Model):
    title       = models.CharField(max_length=250)
    position    = models.IntegerField('Позиция на странице', unique=True)
    name        = models.CharField('Название на странице группы', null=True, blank=True,max_length=250)
    img         = models.ImageField(upload_to='main_page', null=True, blank=True)
    slug        = models.CharField('url', unique=True, null=True, blank=True, max_length=200, help_text='for instance, "mechanisms/meo"' )
    description = HTMLField(null=True, blank=True)
    content     = HTMLField(null=True, blank=True)
    pic_of_hat  = models.ImageField(upload_to='pic_of_hat', null=True, blank=True, help_text='size: 1920x500px')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    parent       = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug_product = models.SlugField('url', help_text='for instance, "40 or 6_3"')
    img          = models.ImageField('Изображение для ссылки', null=True, blank=True, upload_to='mechanisms_preview')
    href_title   = models.CharField(max_length=250)
    name         = models.CharField(max_length=250)
    h1_mod       = models.CharField(max_length=250)
    mod_table    = HTMLField(help_text="Указание идентификатора обязательно. id = 'MOD'")
    description  = HTMLField(null=True, blank=True)
    content      = HTMLField()


    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.href_title)

class ProductImage(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mechanisms', null=True)

    def __str__(self):
        return str(self.page.name)

class DocIcon(models.Model):
    icon = models.TextField(max_length=1000, null=True, blank=True, help_text='bootstrap icons in svg tags')

class ProductDocs(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(upload_to='docs')
    name = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ForeignKey(DocIcon, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.page.name)


class Modification(models.Model):
    parent   = models.ForeignKey(Product, on_delete=models.CASCADE)
    title    = models.CharField(max_length=250, )
    slug_mod = models.SlugField('url', null=True, blank=True, help_text='заполняется автоматически от title')
    content  = HTMLField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    conventional_designation = models.CharField(max_length=250, default=0)

    class Meta:
        ordering = ['parent__id']

    def save(self, *args, **kwargs):
        self.slug_mod = slugify(self.title)
        super(Modification, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
