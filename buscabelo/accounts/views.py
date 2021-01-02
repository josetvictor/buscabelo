from django.shortcuts import render
from .models import Provider
from django.db.models import Q

def index(request):
  return render(request, 'accounts/home.html')
def searchView(request):
  if request.method == 'GET':
    search = request.GET.get('search')
    provider = Provider.objects.all().filter(Q(username__icontains=search) | Q(description__icontains=search))
    return render(request, 'accounts/search.html', {'providers': provider})

