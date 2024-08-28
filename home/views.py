
from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import CollegeModel
from home.serializer import CollegeForm

# Create your views here.

def home(request):
    all_clients = CollegeModel.objects.all()
    context = {'data':all_clients}
    return render(request,'home.html',context)
    
def uploadData(request):
    if request.method=='POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        course = request.POST.get('course')
        address = request.POST.get('address')
        upload_data = CollegeModel(stu_name=name,stu_dob=dob,stu_course=course,address_city=address)
        upload_data.save()
        return redirect('home')
    return render(request,'home.html')


def updateData(request,id):
    if request.method=='POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        course = request.POST.get('course')
        address = request.POST.get('address')

        update_details = CollegeModel.objects.get(id=id)
        update_details.stu_name = name
        update_details.stu_dob = dob
        update_details.stu_course = course
        update_details.address_city = address
        update_details.save()
        
        return redirect('home')
    else:
        update_details = CollegeModel.objects.get(id=id)
        
        context = {'dat':update_details}
        return render(request,'home\edit.html',context)


def deleteData(request,id):
    dela = CollegeModel.objects.get(id=id)
    dela.delete()
    return redirect('/')

