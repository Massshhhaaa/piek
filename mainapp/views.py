from django.shortcuts import render, get_object_or_404
from .models import Categories, Subgroup



def main_def(request):
    categories = Categories.objects.all()
    return render(request, 'mainapp/index.html', context={'categories' : categories})

def SubgroupDetailView(request, slug):
    # queryset = Subgroup.objects.select_related('category__name').values('subgroup__id')#потрачено три часа на эту строчку
    # # q = Subgroup.objects.get(Subgroup pk=pk__in(quryset))
    #
    # # q = Subgroup.objects.filter(pk__in=queryset)
    # print(queryset)
    #
    # categories = Subgroup.objects.all().values('slug')
    # print(categories)
    # q = Subgroup.objects.get(slug=slug__in(categories))
    # print(q)
    c = Subgroup.objects.filter(category__slug=slug).values('pk')
    q = get_object_or_404(Subgroup, pk__in=c)




    return render(request, 'mainapp/SubgroupDetailView.html', context={'q' : q})
