from django.shortcuts import render, redirect, HttpResponse
from main.models import User, User_manager
from events.models import Event, Event_manager
from django.contrib import messages
# Create your views here.
def index(request):
	print("--- index ---")
	return render(request, 'main/index.html')

def about(request):
	print("--- about ---")
	return render(request, 'main/about.html')

def ourteam(request):
	print("--- ourteam ---")
	return render(request, 'main/ourteam.html')

def ourmission(request):
	print("--- our mission ---")
	return render(request, 'main/ourmission.html')

def ourpartners(request):
	print("--- our partners ---")
	return render(request, 'main/ourpartners.html')

def engage(request):
	print("--- engage ---")
	return render(request, 'main/engage.html')

def signup(request):
	print("--- signup ---")
	return render(request, 'main/signup.html')

def register(request):
	print("--- register ---")
	return render(request, 'main/register.html')

def register_user(request, method="POST"):
	print("--- ATTEMPTING register USER ---")
	if request.method == 'POST':
		response_from_models = User.objects.create_user(request.POST)
		if (response_from_models['errors']==0):
			for error in response_from_models.errors:
				messages.error(request, error)
			return redirect("/register")
		else:
			print('--- --------------------------------------------- ---')
			print('--- S U C C E S S F U L _ R E G I S T R A T I O N ---')
			print('--- --------------------------------------------- ---')
			return redirect("/signup")

def login(request, method="POST"):
	print("--- ATTEMPTING login ---")
	response_from_models = User.objects.login_user(request.POST)
	if request.method == 'POST':
		if(response_from_models['errors'] == 0):
			request.session['user_id'] = response_from_models['user'].id
			context = {
				'user': User.objects.get(id=request.session['user_id'])
			}
	return redirect("/")

def yourcommunity(request):
	print("--- your community ---")
	return render(request, 'main/yourcommunity.html')

def getactive(request):
	print("--- get active ---")
	return render(request, 'main/getactive.html')

def tulsa(request):
	print("--- tulsa ---")
	return render(request, 'main/tulsa.html')

def okc(request):
	print("--- okc ---")
	return render(request, 'main/okc.html')

def create_event(request):
	print("--- create_event page ---")
	return render(request, 'main/createevent.html')
