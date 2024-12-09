from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html',)

def consultancies(request):
    return render(request,'consultancies.html')

def events(request):
    return render(request,'events.html')

def offers(request):
    return render(request,'offers.html')

def blog(request):
    return render(request,'blog.html')

def test(request):
    return render(request,'test_prep.html')

def contact(request):
    return render(request,'contact_us.html')



