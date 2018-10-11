from django.http  import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.

# @login_required(login_url='/login/')
def awards(request):
    # post = Image.objects.all()
    return render(request,'awards.html')

def pics(request):
    pictures = Image.objects.all()

    return render(request,'awards.html', {"pictures": pictures})

