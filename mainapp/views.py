from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from mainapp.models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
    context={'categories' : categories,
             'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/index.html', context)

def contacts(request):
    return render(request,'mainapp/contacts.html', context={'in_cart_counter': cart_counter(request)})

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
    mod             = get_object_or_404(Modification, slug_mod=slug_mod, parent__pk__in=product)

    context = {
    'mod' : mod,
    'photos': photos,
    'product_content' : product_content,
    'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/ModificationDetailView.html', context)


def cart(request):
    product_list = None
    if 'piek_cart' in request.session:
        product_list = request.session['piek_cart']
    context = {"product_list": product_list, 'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/cart.html', context)

def certificate(request):
    return render(request, 'mainapp/certificate.html')


def remove_from_cart(request, pk):
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            if pk == int(request.session['piek_cart'][i].get('id')):
                request.session['piek_cart'].pop(i)
                request.session.modified = True
                break
    return redirect('cart')

@require_POST
def update_quantity(request, pk):
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            if pk == int(request.session['piek_cart'][i].get('id')):
                quantity = request.session['piek_cart'][i].get('quantity')
                quantity = int(quantity)
                if 'plus' in request.POST:
                    request.session['piek_cart'][i].update({'quantity': quantity + 1 })
                if 'minus' in request.POST:
                    request.session['piek_cart'][i].update({'quantity': quantity - 1 })
                if 'integer' in request.POST:
                    request.session['piek_cart'][i].update({'quantity': request.POST['integer']})
                request.session.modified = True
                break
    return redirect('cart')

@require_POST
def update_conventional_designation(request, pk):
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            if pk == int(request.session['piek_cart'][i].get('id')):
                context = {'conventional_designation': request.POST['conventional_designation']}
                request.session['piek_cart'][i].update(context)
                request.session.modified = True
                break
    return redirect('cart')

@require_POST
def product(request, pk):
    product_title = Modification.objects.only('title').get(id=pk)
    print(product_title)
    print(pk)
    if 'piek_cart' not in request.session:
        request.session['piek_cart']= []
    if pk not in request.session['piek_cart']:
        context={'title': str(product_title),
                 'quantity': request.POST['quantity'],
                 'id': pk,
                }
        request.session['piek_cart'].append(context)
        request.session.modified = True
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)

def checkout(request):
    product_list = None
    if 'piek_cart' in request.session:
        product_list = request.session['piek_cart']
    context = {"product_list": product_list, "in_cart_counter": cart_counter(request)}
    return render(request, 'mainapp/checkout.html', context)

@require_POST
def sent_mail(request):
    product_list = request.session['piek_cart']
    subject = " ООО ПЭК | Заказ "
    html_template = 'mainapp/html_message.html'
    from_email = "kondensat01@gmail.com"
    to_email = request.POST['email']
    name = request.POST['firstname']

    html_message = render_to_string(html_template, { 'product_list': product_list, 'name' : name, })

    message = EmailMessage(subject, html_message, from_email, [to_email])
    message.content_subtype = 'html'
    message.send()
    request.session['piek_cart'].clear()
    request.session.modified = True
    return render(request, 'mainapp/minor/sent_mail.html')


def cart_counter(request):
    counter = 0
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            counter += int(request.session['piek_cart'][i].get('quantity'))
    return counter
