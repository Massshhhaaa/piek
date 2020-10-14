from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from mainapp.models import *
from mainapp.views_cart import *
import mainapp.views_cart
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
