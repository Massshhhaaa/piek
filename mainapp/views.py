from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from mainapp.models import *
from mainapp.views_cart import *
import mainapp.views_cart
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
    context={'categories' : categories,
             'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/index.html', context)

def SubgroupDetailView(request, slug):
    subgroup_info = get_object_or_404(Group, slug=slug)
    product_list  = Product.objects.filter(parent__slug=slug)
    return render(
    request,
    'mainapp/SubgroupDetailView.html',
    context = {
    'subgroup_info' : subgroup_info,
    'product_list'  : product_list,
    'in_cart_counter': cart_counter(request),
    })


def ProductDetailView(request, slug_product, slug):
    session_id = request.session._get_or_create_session_key()
    product  = Product.objects.get(parent__slug=slug, slug_product=slug_product)
    photos   = ProductImage.objects.filter(page = product)
    docs     = ProductDocs.objects.filter(page = product)
    mod_list = Modification.objects.only('title', 'slug_mod','id').filter(parent__parent__slug=slug, parent__slug_product=slug_product)

    context = {
    'product' : product,
    'photos': photos,
    'docs': docs,
    'mod_list' : mod_list,
    'in_cart_counter': cart_counter(request),
    }
    return render(request, 'mainapp/ProductDetailView.html', context)


def ModificationDetailView(request, slug, slug_product, slug_mod):
    product         = Product.objects.filter(parent__slug=slug, slug_product=slug_product).values('pk')
    product_content = Product.objects.only('content', 'href_title', 'h1_mod').get(pk__in = product)
    photos          = ProductImage.objects.filter(page__pk__in=product)
    docs            = ProductDocs.objects.filter(page__pk__in=product)
    mod             = get_object_or_404(Modification, slug_mod=slug_mod, parent__pk__in=product)

    context = {
    'mod' : mod,
    'photos': photos,
    'docs' : docs,
    'product_content' : product_content,
    'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/ModificationDetailView.html', context)

def contacts(request):
    return render(request,'mainapp/contacts.html', context={'in_cart_counter': cart_counter(request)})

def about(request):
    return render(request, 'mainapp/about.html', {'in_cart_counter': cart_counter(request),})

def certificate(request):
    return render(request, 'mainapp/certificate.html', {'in_cart_counter': cart_counter(request),})

def docs(request):
    return render(request, 'mainapp/docs/operation-manuals.html', {'in_cart_counter': cart_counter(request),})

def general_industrial_design(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/general_industrial_design.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def explosion_proof_design(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/explosion_proof_design.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def sensors_and_controllers(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/sensors_and_controllers.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def starting_and_control_devices(request):
    return render(request, 'mainapp/docs/starting_and_control_devices.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def barriers(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/barriers.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
