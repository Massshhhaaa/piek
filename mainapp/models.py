from django.db import models
import tinymce 

# Create your models here.

class Categories(models.Model):
    name = models.CharField('Категория', max_length=250)
    img = models.ImageField(upload_to='static/img/main_page', null=True, blank=True)
    slug = models.SlugField('url', unique=True)

    def __str__(self):
        return self.name
#
#
# class Person(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     img = models.ImageField(upload_to='static/img', null=True, blank=True)
#     team_role = models.CharField('Командная роль', max_length=50, null=True,)
#     about = models.CharField('О себе', max_length=255, null=True,)
#
#
#     def __str__(self):
#         return '%s %s %s' % (self.first_name, self.last_name, self.team.name)
#
#
#
# class Hello(models.Model):
#     team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True)
#     title = models.CharField('Название', max_length=250)
#     slug = models.CharField('url', unique=True, max_length=250)
#     img = models.ImageField(upload_to='static/img', null=False, blank=False)
#     excerption = models.CharField('Отрывок', max_length=255)
#     annotation = models.TextField('Аннотация')
#     text = HTMLField()
#
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
#
#
#
#
#
#
# def slug_generator(sender, instance, *args,**kwargs):
#     if not instance.slug:
#         instance.slug = 'SLUG'
#
# pre_save.connect(slug_generator, sender=Hello)
