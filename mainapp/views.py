from django.shortcuts import render, get_object_or_404
from mainapp.models import Group, SubgroupImage, Product, ProductImage


def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
    return render(request, 'mainapp/index.html', context={'categories' : categories})

def contacts(request):
    return render(request,'mainapp/contacts.html')

def SubgroupDetailView(request, slug):
    subgroup_info = get_object_or_404(Group, slug=slug)
    photos = SubgroupImage.objects.filter(page = subgroup_info)
    product_list = Product.objects.filter(parent__slug=slug)
    return render(
    request,
    'mainapp/SubgroupDetailView.html',
    context={
    'subgroup_info' : subgroup_info,
    'photos': photos,
    'product_list': product_list,
    })



def ProductDetailView(request, slug_product, slug):
    product = Product.objects.filter(parent__slug=slug).filter(slug_product=slug_product)
    photos = ProductImage.objects.filter(page = product)
    return render(request, 'mainapp/ProductDetailView.html', context={'product' : product, 'photos': photos})
