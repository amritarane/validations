from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
        #     sname=SFDO.cleaned_data['sname']
        #     sid=SFDO.cleaned_data['sid']
        #     sage=SFDO.cleaned_data['sage']
        #     semail=SFDO.cleaned_data['semail']
        #     sremail=SFDO.cleaned_data['sremail']
        #     s=Student.objects.get_or_create(sname=sname,sid=sid,sage=sage,semail=semail,sremail=sremail)[0]
        #     s.save()
        #     QSSO=Student.objects.all()
        #     a={'QSSO':QSSO}
        #     return render(request,'display_student.html',a)
            return HttpResponse(str(SFDO.cleaned_data) )
        else:
            return HttpResponse('Invalid data')


    return render(request,'student.html',d)