from django.db import models
from pytils.translit import slugify
from tinymce import HTMLField

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


class Modification(models.Model):
    parent   = models.ForeignKey(Product, on_delete=models.CASCADE)
    title    = models.CharField(max_length=250, )
    slug_mod = models.SlugField('url', null=True, blank=True, help_text='заполняется автоматически от title')
    content  = HTMLField(null=True, blank=True)

    class Meta:
        ordering = ['parent__id']

    def save(self, *args, **kwargs):
        self.slug_mod = slugify(self.title)
        super(Modification, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	device = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)



class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Modification, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
