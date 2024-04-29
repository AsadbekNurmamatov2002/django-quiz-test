from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm, ProfileEditForm, UserEditForm
from django.contrib import messages
# Create your views here.

def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST,instance=request.user)
        profile_form = ProfileEditForm(request.POST,request.FILES ,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() and profile_form.save()
            return redirect('quizes:quizlist')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        # return redirect('quizes:quizlist')
    return render(request,'authuser/edit.html', {'user_form': user_form,'profile_form': profile_form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect('quizes:quizlist')
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, template_name="authuser/login.html", context={"form":form})


def register_request(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("quizes:quizlist")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomUserCreationForm()
	return render (request=request, template_name="authuser/RegisterPage.html", context={"form":form})


def LogoutPage(request):
    if request.POST:
        logout(request)
        return redirect('users:login')
    else:
        return render(request, 'logout.html',{})