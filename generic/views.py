from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,'one.html')

def second(request):
    return render(request,'second.html')