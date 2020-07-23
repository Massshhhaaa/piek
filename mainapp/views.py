from django.shortcuts import render, get_object_or_404
from .models import Categories, Subgroup



def main_def(request):
    categories = Categories.objects.all()
    return render(request, 'mainapp/index.html', context={'categories' : categories})

def SubgroupDetailView(request, slug):
    queryset = Subgroup.objects.select_related('category__slug')#потрачено три часа на эту строчку
    q = Subgroup.get_object_or_404(Subgroup)



    return render(request, 'mainapp/SubgroupDetailView.html', context={'queryset' : queryset, 'q':q})
