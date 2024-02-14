from django.shortcuts import render
from app.models import *

# Create your views here.
def Retrivingdata(request):
    QLDO=Dept.objects.all()
    d={'depts':QLDO}
    return render(request,'Retrivingdata.html',d) 
