from django.db import models
from pytils.translit import slugify
from tinymce import HTMLField
from django.shortcuts import reverse
from multiselectfield import MultiSelectField

SENSOR_CHOICES = (('М', 'М'),
               ('У', 'У'),
               ('Р', 'Р'),
               ('И', 'И'),
               ('БЦА', 'БЦА'))

class Group(models.Model):
    title       = models.CharField(max_length=250)
    position    = models.IntegerField('Позиция на странице', unique=True)
    meta_description = models.TextField(null=True, blank=True)
    name        = models.CharField('Название на странице группы', null=True, blank=True,max_length=250)
    img         = models.ImageField(upload_to='main_page', null=True, blank=True)
    slug        = models.CharField('url', unique=True, null=True, blank=True, max_length=200, help_text='for instance, "mechanisms/meo"' )
    description = HTMLField(null=True, blank=True)
    content     = HTMLField(null=True, blank=True)
    pic_of_hat  = models.ImageField(upload_to='pic_of_hat', null=True, blank=True, help_text='size: 1920x500px')
    dark_banner = models.BooleanField(default=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('SubgroupDetailView', args=[self.slug])

class Documentation(models.Model):
    key_filter = models.CharField(max_length=20)
    key_sort = models.IntegerField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=255)
    file = models.FileField()

    class Meta:
        ordering = ['key_sort']

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    parent       = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug_product = models.SlugField('url', help_text='for instance, "40 or 6_3"')
    meta_description = models.TextField(null=True, blank=True)
    img          = models.ImageField('Изображение для ссылки', upload_to='mechanisms_preview')
    href_title   = models.CharField("title group", max_length=250,)
    name         = models.CharField(max_length=250)
    h1_mod       = models.CharField(max_length=250)
    mod_table    = HTMLField(help_text="Указание идентификатора обязательно. id = 'MOD'")
    description  = HTMLField('description group', null=True, blank=True)
    content      = HTMLField()
    sensors       = MultiSelectField(choices=SENSOR_CHOICES, max_choices=10, max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.href_title)

    def get_absolute_url(self):
        return reverse('ProductDetailView', kwargs={'slug':self.parent.slug,'slug_product':self.slug_product})

class ProductImage(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mechanisms', null=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return str(self.page.name)

class ProductDocs(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item = models.ForeignKey(Documentation, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.page.name)



class Modification(models.Model):
    parent           = models.ForeignKey(Product, on_delete=models.CASCADE)
    title            = models.CharField(max_length=250, )
    slug_mod         = models.SlugField('url', null=True, blank=True, help_text='заполняется автоматически от title')
    content          = HTMLField(null=True, blank=True)

    class Meta:
        ordering = ['parent__id']

    def get_absolute_url(self):
        return reverse('ModificationDetailView', kwargs={'slug':self.parent.parent.slug,'slug_product':self.parent.slug_product,'slug_mod':self.slug_mod})

    def save(self, *args, **kwargs):
        self.slug_mod = slugify(self.title)
        super(Modification, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


# этот класс содержит все варианты датчиков для исполнительных механизмов
# Данные из этого класс вытягиваются на страница продукта, модификации
class Sensors(models.Model):
    character   = models.CharField(choices=SENSOR_CHOICES, max_length=250)
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    file        = models.FileField()


    def __str__(self):
        return str(self.name)
