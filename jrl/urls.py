"""jrl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_def, name='main_def'),
    path('contacts/', contacts, name='contacts'),
    path('admin/', admin.site.urls),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('sent_mail/', sent_mail, name="sent_mail"),
    path('product/<int:pk>', product, name='product'), # this using as add-to-cart
    path('remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:pk>', update_quantity, name='update_quantity'),
    path('update_conventional_designation/<int:pk>', update_conventional_designation, name='update_conventional_designation'),


    path('catalog/<path:slug>/info/<slug:slug_product>/<slug:slug_mod>', ModificationDetailView),

    path('catalog/<path:slug>/info/<slug:slug_product>/', ProductDetailView, name='ProductDetailView'),

    path('catalog/<path:slug>/', SubgroupDetailView, name='SubgroupDetailView'),


    path('tinymce/', include('tinymce.urls')),
    path('jet_api/', include('jet_django.urls')),
    # path('about/', about, name='about'),
    # path('about/gallery/', about_gallery, name='about_gallery'),
    #
    # path('docs/', docs_list, name='docs_list'),
    # path('docs/questionnaire/', docs_questionnaire, name='docs_questionnaire'),
    #


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
