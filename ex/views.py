from django.shortcuts import render, get_object_or_404
from .models import star

# Create your views here.
def home(request):
    stars = star.objects
    return render(request, 'home.html',{'stars': stars})

def detail(request, star_id):
    star_detail = get_object_or_404(star, pk=star_id)
    return render(request, 'detail.html', {'star': star_detail})