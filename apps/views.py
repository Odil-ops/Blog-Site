from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User


def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	if request.method == 'POST':
		phone = request.POST.get('phone')
		password = request.POST.get('password')
		
		try:
			user = User.objects.get(phone=phone)
			user = authenticate(request, username=user.username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"Xush kelibsiz, {user.username}!")
				return redirect('home')
			else:
				messages.error(request, "Parol xato!")
		except User.DoesNotExist:
			messages.error(request, "Telefon raqami topilmadi!")
	
	return render(request, 'login.html')


def register_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	if request.method == 'POST':
		username = request.POST.get('username')
		phone = request.POST.get('phone')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		
		if password != password2:
			messages.error(request, "Parollar bir-biriga mos kelmadi!")
			return render(request, 'register.html')
		
		if User.objects.filter(phone=phone).exists():
			messages.error(request, "Bu telefon raqami allaqachon ro'yxatdan o'tgan!")
			return render(request, 'register.html')
		
		if User.objects.filter(username=username).exists():
			messages.error(request, "Bu ism allaqachon olingan!")
			return render(request, 'register.html')
		
		user = User.objects.create_user(username=username, phone=phone, password=password)
		messages.success(request, "Ro'yxatdan o'tish muvaffaqiyatli! Endi kiring.")
		return redirect('login')
	
	return render(request, 'register.html')


def logout_view(request):
	logout(request)
	messages.success(request, "Chiqish muvaffaqiyatli!")
	return redirect('login')


# Page views that render the corresponding templates.
@login_required(login_url='login')
def index(request):
	return render(request, 'index.html')


@login_required(login_url='login')
def about(request):
	return render(request, 'about.html')


@login_required(login_url='login')
def blog(request):
	return render(request, 'blog.html')


@login_required(login_url='login')
def contact(request):
	return render(request, 'contact.html')


@login_required(login_url='login')
def feature(request):
	return render(request, 'feature.html')


@login_required(login_url='login')
def menu(request):
	return render(request, 'menu.html')


@login_required(login_url='login')
def team(request):
	return render(request, 'team.html')


@login_required(login_url='login')
def testimonial(request):
	return render(request, 'testimonial.html')


@login_required(login_url='login')
def loxotron(request):
	return render(request, 'main/loxotron.html')


def page_not_found(request, exception=None):
	return render(request, '404.html', status=404)
