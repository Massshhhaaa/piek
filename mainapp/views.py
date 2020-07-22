from django.shortcuts import render, get_object_or_404
from .models import Categories


# Create your views here.
def main_def(request):
    categories = Categories.objects.all()
    return render(request, 'mainapp/index.html', context={'categories' : categories})

def SubgroupDetailView(request, slug):
    queryset = get_object_or_404(Categories, slug= slug)
    return render(request, 'mainapp/index.html', context={'queryset' : queryset})
