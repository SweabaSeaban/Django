from django.shortcuts import render
from django.http import HttpResponse
from .models import Home
# Create your views here.
def home(request):
    details=Home.objects.all()
    return render(request,'index.html',{'details':details})