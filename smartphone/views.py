from django.shortcuts import render
from .models import Smartphone
# Create your views here.
def smartphone(request):
    smartphones = Smartphone.objects.all()
    return render(request,'smartphone.html',context={'smartphones':smartphones})

def smartphone_det(request,pk):
    smartphone =Smartphone.objects.get(id=pk)
    return render(request,'smartphone_det.html',context={'smartphone':smartphone})


    
    