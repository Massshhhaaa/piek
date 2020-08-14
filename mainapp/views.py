from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import ListView, DetailView, View
from mainapp.models import *


def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
    m = request.session._get_or_create_session_key()
    print(m)
    return render(request, 'mainapp/index.html', context={'categories' : categories})

def contacts(request):
    return render(request,'mainapp/contacts.html')

def SubgroupDetailView(request, slug):
    subgroup_info = get_object_or_404(Group, slug=slug)
    product_list  = Product.objects.filter(parent__slug=slug)
    return render(
    request,
    'mainapp/SubgroupDetailView.html',
    context = {
    'subgroup_info' : subgroup_info,
    'product_list'  : product_list,
    })


def ProductDetailView(request, slug_product, slug):
    product  = Product.objects.get(parent__slug=slug, slug_product=slug_product)
    photos   = ProductImage.objects.filter(page = product)
    mod_list = Modification.objects.only('title', 'slug_mod','id').filter(parent__parent__slug=slug, parent__slug_product=slug_product)

    device = request.COOKIES['device']
    customer= Customer.objects.get(device=device)
    order = Order.objects.get(customer=customer, complete=False)

    context = {
    'product' : product,
    'photos': photos,
    'mod_list' : mod_list,
    'order':order,
    }
    return render(request, 'mainapp/ProductDetailView.html', context)


def ModificationDetailView(request, slug, slug_product, slug_mod):
    product         = Product.objects.filter(parent__slug=slug, slug_product=slug_product).values('pk')
    product_content = Product.objects.only('content', 'href_title', 'h1_mod').get(pk__in = product)
    photos          = ProductImage.objects.filter(page__pk__in=product)
    mod             = get_object_or_404(Modification, slug_mod=slug_mod, parent__pk__in=product)

    context = {
    'mod' : mod,
    'photos': photos,
    'product_content' : product_content,}
    return render(request, 'mainapp/ModificationDetailView.html', context)


def product(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Modification, id=pk)

        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

def remove_from_cart(request, pk):
    product = get_object_or_404(Modification, id=pk)
    device = request.COOKIES['device']
    customer = Customer.objects.get(device=device)

    order = Order.objects.get(customer=customer, complete=False)
    orderItem = OrderItem.objects.get(order=order, product=product)
    orderItem.delete()

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(reverse('cart'))


def cart(request):
	device = request.COOKIES['device']
	customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	context = {'order':order}
	return render(request, 'mainapp/cart.html', context)
