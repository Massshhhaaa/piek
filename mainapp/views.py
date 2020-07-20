from django.shortcuts import render, get_object_or_404
from .models import Categories


# Create your views here.
def main_def(request):
    return render(request, 'mainapp/index.html', context={'categories' : Categories.objects.all()})

# def detail(request, slug):
#     post = get_object_or_404(Hello, slug = slug)
#     return render(request, "mainapp/post.html", {'post': post})
#
#
# def team_view(request):
#     teams= Team.objects.all()
#     persons = Person.objects.all()
#     return render(request, 'mainapp/teams.html', context={'teams' :teams, 'persons' :persons})
