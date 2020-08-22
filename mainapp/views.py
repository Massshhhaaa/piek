from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_POST
from django.conf import settings
from mainapp.models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
    print(request.session.items())
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


    customer, created = Customer.objects.get_or_create(device=session_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    mods_in_cart = request.session.keys()
    context = {
    'product' : product,
    'photos': photos,
    'docs': docs,
    'mod_list' : mod_list,
    'order':order,
    'mods_in_cart' : mods_in_cart,#not using now
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
    context = {"product_list": product_list, "counter": counter, 'in_cart_counter': cart_counter(request),}
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

def checkout(request):
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
    return render(request, 'mainapp/checkout.html', context)

@require_POST
def sent_mail(request):
    id = list(request.session.keys())
    quantity = list(request.session.items())
    product_list = Modification.objects.filter(pk__in=id)
    counter = cart_counter(request)

    subject = " ООО ПЭК | Заказ "
    html_template = 'mainapp/html_message.html'
    from_email = "kondensat01@gmail.com"
    to_email = request.POST['email']
 # я тебя прекрасно понимаю, что то что находится ниже вызывает некоторые вопросы.
 # я использую поля бд для временного хранения данных, но я не сохраняю их в бд. да это тупо. но так код чище
 # я беру их из сессии сопоставляю по id и пихаю в эти поля quantity и conventional_designation и теперь они становятся частью коллекции
 # поэтому можешь обращаться к этим полям в цикле как product.quantity и product.conventional_designation
    for product in product_list:
        for i in range(len(quantity)):
            if int(quantity[i][0]) == product.id:
                product.quantity = int(quantity[i][1].get('quantity'))
                product.conventional_designation = quantity[i][1].get('conventional_designation')

    html_message = render_to_string(html_template, { 'product_list': product_list, })

    message = EmailMessage(subject, html_message, from_email, [to_email])
    message.content_subtype = 'html' # this is required because there is no plain text email message
    message.send()


def cart_counter(request):
    quantity = list(request.session.items())
    counter=0
    for i in range(len(quantity)):
        counter += int(quantity[i][1].get('quantity'))
    return counter
