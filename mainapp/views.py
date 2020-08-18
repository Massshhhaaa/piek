from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_POST
from django.conf import settings
from mainapp.models import *


def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
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
    session_id = request.session._get_or_create_session_key()
    product  = Product.objects.get(parent__slug=slug, slug_product=slug_product)
    photos   = ProductImage.objects.filter(page = product)
    mod_list = Modification.objects.only('title', 'slug_mod','id').filter(parent__parent__slug=slug, parent__slug_product=slug_product)

    customer, created = Customer.objects.get_or_create(device=session_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    mods_in_cart = request.session.keys()
    context = {
    'product' : product,
    'photos': photos,
    'mod_list' : mod_list,
    'order':order,
    'mods_in_cart' : mods_in_cart,
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


def cart(request):
    id = list(request.session.keys())
    quantity = list(request.session.items())
    product_list = Modification.objects.filter(pk__in=id)
    counter = 0
    for product in product_list:
        for i in range(len(quantity)):
            if int(quantity[i][0]) == product.id:
                product.quantity = int(quantity[i][1].get('quantity'))
                product.conventional_designation = quantity[i][1].get('conventional_designation')
                counter += int(quantity[i][1].get('quantity'))
    context = {"product_list": product_list, "counter": counter}
    return render(request, 'mainapp/cart.html', context)

def remove_from_cart(request, pk):
    # product = get_object_or_404(Modification, id=pk)
    # session_id = request.session._get_or_create_session_key()
    # customer = Customer.objects.get(device=session_id)
    #
    # order = Order.objects.get(customer=customer, complete=False)
    # orderItem = OrderItem.objects.get(order=order, product=product)
    # orderItem.delete()
    del request.session[str(pk)]
    request.session.modified = True
    return redirect('cart')

@require_POST
def update_quantity(request, pk):
    quantity = request.session[str(pk)].get('quantity')
    print(quantity)
    quantity = int(quantity)
    if 'plus' in request.POST:
        print("урааааа")
        request.session[str(pk)].update({'quantity': quantity + 1 })
    if 'minus' in request.POST:
        request.session[str(pk)].update({'quantity': quantity - 1 })
    if 'integer' in request.POST:
        request.session[str(pk)].update({'quantity': request.POST['integer']})
    request.session.modified = True
    return redirect('cart')

@require_POST
def update_conventional_designation(request, pk):
    if 'conventional_designation' in request.POST:
        request.session[str(pk)].update({'conventional_designation': request.POST['conventional_designation']})
        request.session.modified = True
    return redirect('cart')

@require_POST
def product(request, pk):
    # cart = Cart(request)
    # product = get_object_or_404(Modification, id=pk)
    # cart.add(pk=product, quantity=request.POST['quantity'])

    if pk not in request.session:
        request.session[str(pk)]= {'quantity': request.POST['quantity']}
    if pk not in request.session:
        request.session[str(pk)] = {'quantity': request.POST['quantity']}
        # product = get_object_or_404(Modification, id=pk)
        # customer, created = Customer.objects.get_or_create(device=session_id)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        # orderItem.quantity=request.POST['quantity']
        # orderItem.save()

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
