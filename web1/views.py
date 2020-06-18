from django.shortcuts import render
from web1.models import Team
from django.http import HttpResponse
# Create your views here.

def index(request):

    members = Team.objects.all()

    return render(request, 'index.html', {'members': members})


