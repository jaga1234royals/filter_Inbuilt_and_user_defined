from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data':'mY nAmE Is jAGaDeESh'}
    return render(request,'filters.html',d)

def userdefinedfilters(request):
    d={'data':'mY nAmE Is jAGaDeESh'}
    return render(request,'userdefinedfilters.html',d)
