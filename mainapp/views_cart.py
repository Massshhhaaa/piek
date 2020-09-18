from django.views.decorators.http import require_POST

def cart(request):
    product_list = None
    if 'piek_cart' in request.session:
        product_list = request.session['piek_cart']
    context = {"product_list": product_list, 'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/cart.html', context)

def checkout(request):
    product_list = None
    if 'piek_cart' in request.session:
        product_list = request.session['piek_cart']
    context = {"product_list": product_list, "in_cart_counter": cart_counter(request)}
    return render(request, 'mainapp/checkout.html', context)

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
    if 'piek_cart' not in request.session:
        request.session['piek_cart']= []
    existance_in_cart = True
    #Проверка на то есть ли в корзину уже данный pk(id)
    for i in range(0, len(request.session['piek_cart'])):
        if  pk == request.session['piek_cart'][i].get('id'):
            quantity = request.session['piek_cart'][i].get('quantity')
            quantity = int(quantity)
            request.session['piek_cart'][i].update({'quantity': quantity + 1 })
            request.session.modified = True
            existance_in_cart = False
            break
    #Если после проверки его там нет то existance_in_cart останется как True и он добавится
    if existance_in_cart:
        context={'title': str(product_title),
                 'quantity': request.POST['quantity'],
                 'id': pk,
                }
        request.session['piek_cart'].append(context)
        request.session.modified = True
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)



@require_POST
def sent_mail(request):
    product_list = request.session['piek_cart']
    subject = " ООО ПЭК | Заказ "
    html_template = 'mainapp/html_message.html'
    from_email = "pr@piek.ru"
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
