from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Checkins
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request,'home.html')

def checkins_list(request):
	if request.method=='POST':
		code = request.POST['latitude'] + ' ' + request.POST['longitude'] + ' ' + request.POST['review']
		checkin=Checkins(latitude=request.POST['latitude'],longitude=request.POST['longitude'],review=request.POST['review'],place_name=request.POST['place_name'],updated_by=request.user)
		checkin.save()
	checkins=Checkins.objects.filter(updated_by=request.user)
	return render(request,'checkin_list.html',{'checkins':checkins})

def signup(request):
	return render(request,'signup.html')


def test(request):
    current_user=request.user
    return HttpResponse(current_user.email)

def delete_record(request):
    id=request.POST['id']
    Checkins.objects.filter(id=id).delete()
    checkins = Checkins.objects.filter(updated_by=request.user)
    return render(request, 'checkin_list.html', {'checkins': checkins})

def update_record(request):
    id=request.POST['id']
    place_name=request.POST['place_name']
    review=request.POST['review']
    record=Checkins.objects.filter(id=id)
    record.place_name=place_name
    record.review=review
    record.save()
    checkins = Checkins.objects.filter(updated_by=request.user)
    return render(request, 'checkin_list.html', {'checkins': checkins})







	