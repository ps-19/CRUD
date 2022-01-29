from asyncio.windows_events import NULL
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# This Function Will Create New Data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm = StudentRegistration()
    students = User.objects.all()
    return render(request, 'enroll/editAndShow.html', {'form': fm, 'total_data': students})
    # total data tranferred


#This Function Will Delete Any Data
def delete_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/')


#This Function Will Update Any Data
def update_data(request, id):                            # update argument
    data = User.objects.get(pk=id)
    return render(request, 'enroll/update.html', {'data': data})