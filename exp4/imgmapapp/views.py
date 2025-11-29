from django.shortcuts import render
def imgmap(request):
    return render(request,'imagemap.html')
def manyavarclothing(request):
    return render(request,'manyavar.html')
def bs(request):
    return render(request,'bluestone.html')
def mcdonalds(request):
    return render(request,'mcd.html')
def tz(request):
    return render(request,'timezone.html')
    