from django.shortcuts import render, get_object_or_404
from mainapp.models import Group, Product, ProductImage, Modification


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
    product = Product.objects.get(parent__slug=slug, slug_product=slug_product)
    photos = ProductImage.objects.filter(page = product)
    mod_list = Modification.objects.only('title', 'slug_mod').filter(parent__parent__slug=slug, parent__slug_product=slug_product)
    print(mod_list)
    return render(request,
    'mainapp/ProductDetailView.html',
    context = {'product' : product, 'photos': photos, 'mod_list' : mod_list})


def ModificationDetailView(request, slug, slug_product, slug_mod):
    product         = Product.objects.filter(parent__slug=slug, slug_product=slug_product).values('pk')
    product_content = Product.objects.only('content', 'href_title', 'h1_mod').get(pk__in = product)
    photos          = ProductImage.objects.filter(page__pk__in=product)
    mod             = get_object_or_404(Modification, slug_mod=slug_mod, parent__pk__in=product)
    return render(
    request,
    'mainapp/ModificationDetailView.html',
     context = {
    'mod' : mod,
    'photos': photos,
    'product_content' : product_content,})
