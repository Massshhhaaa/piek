from django.shortcuts import render, get_object_or_404
from mainapp.models import Categories, Subgroup, SubgroupImage, Product, ProductImage



def main_def(request):
    categories = Categories.objects.all()
    return render(request, 'mainapp/index.html', context={'categories' : categories})

def contacts(request):
    return render(request,'mainapp/contacts.html')

def SubgroupDetailView(request, slug):
    c = Subgroup.objects.filter(category__slug=slug).values('pk')
    subgroup_info = Subgroup.objects.get(pk__in=c)
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
