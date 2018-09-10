from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Checkins

# Create your views here.
def home(request):
	return render(request,'map2.html')

def checkins_list(request):
	if request.method=='POST':
		code = request.POST['latitude'] + ' ' + request.POST['longitude'] + ' ' + request.POST['review']
		checkin=Checkins(latitude=request.POST['latitude'],longitude=request.POST['longitude'],review=request.POST['review'])
		checkin.save()
	checkins=Checkins.objects.all()
	return render(request,'checkin_list.html',{'checkins':checkins})

def test(request):
	return render(request,'map2.html')

def signup(request):
	return render(request,'signup.html')

def output(request):
	code='Nothing is received'
	if request.method=='POST':
		code = request.POST['latitude'] + ' ' + request.POST['longitude'] + ' ' + request.POST['review']
		checkin=Checkins(latitude=request.POST['latitude'],longitude=request.POST['longitude'],review=request.POST['review'])
		checkin.save()

	return HttpResponse(code)



	