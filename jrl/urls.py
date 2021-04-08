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
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from mainapp.sitemaps import StaticViewSitemap, GroupsSitemap, ProductsSitemap, ModificationsSitemap

sitemaps = {
    'static' : StaticViewSitemap,
    'group' : GroupsSitemap,
    'product': ProductsSitemap,
    'modification': ModificationsSitemap
}

urlpatterns = [
    path('', main_def, name='main_def'),
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('tinymce/', include('tinymce.urls')),

    path("robots.txt", TemplateView.as_view(template_name="mainapp/minor/robots.txt", content_type="text/plain"),),

    path('contacts/', contacts, name='contacts'),
    path('cart/', cart, name="cart"),
    path('about/', about, name="about"),
    path('docs/', docs, name='docs'),
    path('certificates/', certificate, name='certificate'),

    path('sensors/', sensors, name="sensors"),

    path('docs/general-industrial-design/', general_industrial_design, name='general_industrial_design'),
    path('docs/explosion-proof-design/', explosion_proof_design, name='explosion_proof_design'),
    path('docs/sensors-and-controllers/', sensors_and_controllers, name='sensors_and_controllers'),
    path('docs/starting-and-control-devices/', starting_and_control_devices, name='starting_and_control_devices'),
    path('docs/barriers/', barriers, name='barriers'),

    path('checkout/', checkout, name="checkout"),
    path('sent_mail/', sent_mail, name="sent_mail"),
    path('ajax/product/<int:pk>', product, name='product'), # this using as add-to-cart
    path('ajax/remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
    path('ajax/update_quantity/<int:pk>', update_quantity, name='update_quantity'),
    path('ajax/update_conventional_designation/<int:pk>', update_conventional_designation, name='update_conventional_designation'),


    path('<path:slug>/<slug:slug_product>/<slug:slug_mod>', ModificationDetailView, name='ModificationDetailView'),
    path('<path:slug>/<slug:slug_product>/', ProductDetailView, name='ProductDetailView'),
    path('<path:slug>/', SubgroupDetailView, name='SubgroupDetailView'),
    ]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
