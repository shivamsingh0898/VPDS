from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .forms import UserForm, SignUpForm
from django.shortcuts import render, redirect
from .models import *


@login_required(login_url='dashboard/login/')
def index(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = VpmUser.objects.filter(user__is_superuser=True)
        all_proj2 = VpmUser.objects.filter(user__groups=2)
        user_count = User.objects.annotate(count=Count('id'))
        proj_count = ProjectArchive.objects.annotate(count=Count('id'))
        active_proj_count = LiveProject.objects.annotate(count=Count('id'))
        hold_proj_count = ProjectsOnHold.objects.annotate(count=Count('id'))
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar, 'user_count': user_count, 'proj_count': proj_count, 'active_proj_count' : active_proj_count, 'hold_proj_count': hold_proj_count, 'all_proj': all_proj, 'all_proj2': all_proj2}
    return render(request, 'dashboard/index.html', context)


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard:index')
            else:
                return render(request, 'dashboard/log-in.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dashboard/log-in.html', {'error_message': 'Invalid login'})
    return render(request, 'dashboard/log-in.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'dashboard/log-in.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard:login')
    else:
        form = SignUpForm()
    return render(request, 'dashboard/signup.html', {'form': form})


def account(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = ProjectArchive.objects.all()
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            address = obj.address
            designation = obj.specialization
            email = obj.user.email
            phone = obj.phone
            context = {'name': name, 'avatar': avatar, 'address': address, 'designation': designation, 'email': email,
                       'phone': phone, 'all_proj': all_proj}
    return render(request, 'dashboard/account.html', context)


def admin(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = VpmUser.objects.filter(user__is_superuser=True)
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar, 'all_proj': all_proj}
    return render(request, 'dashboard/admin.html', context)


def developer(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = VpmUser.objects.filter(user__groups=2)
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar, 'all_proj': all_proj}
    return render(request, 'dashboard/developer.html', context)


def project_manager(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = VpmUser.objects.filter(user__groups=1)
        all_object = VpmUser.objects.filter(user=request.user)
        for obj1 in all_object:
            f_name = obj1.user.first_name
            l_name = obj1.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj1.avatar
            context = {'name': name, 'avatar': avatar, 'all_proj': all_proj}
    return render(request, 'dashboard/project-manager.html', context)


def live_project(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = LiveProject.objects.all()
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar, 'all_proj': all_proj}
    return render(request, 'dashboard/live-project.html', context)


def project_archive(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = ProjectArchive.objects.all()
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar, 'all_proj': all_proj}
    return render(request, 'dashboard/project-archive.html', context)


def project_hold(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_proj = ProjectsOnHold.objects.all()
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar, 'all_proj': all_proj}
    return render(request, 'dashboard/project-hold.html', context)


def contact(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_object = VpmUser.objects.filter(user=request.user)
        all_contact = Contact.objects.filter(id=1)
        for obj, obj2 in zip(all_object, all_contact):
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            tittle = obj2.tittle
            ph_no1 = obj2.ph_no1
            address = obj2.corp_address
            email1 = obj2.email1
            context = {'name': name, 'avatar': avatar, 'tittle': tittle, 'address': address, 'phone_no1': ph_no1,
                       'email1': email1}
    return render(request, 'dashboard/contact.html', context)


'''def technical_support(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar}
    return render(request, 'dashboard/technical-support.html', context)'''


def about(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_object = VpmUser.objects.filter(user=request.user)
        about_us = About.objects.filter(id=1)
        for obj, obj2 in zip(all_object, about_us):
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            tittle = obj2.tittle
            body = obj2.body
            context = {'name': name, 'avatar': avatar, 'tittle': tittle, 'body': body}
    return render(request, 'dashboard/about.html', context)


'''def feedback(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar}
    return render(request, 'dashboard/feedback.html', context)'''


'''def ratings(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'dashboard/log-in.html')
    else:
        all_object = VpmUser.objects.filter(user=request.user)
        for obj in all_object:
            f_name = obj.user.first_name
            l_name = obj.user.last_name
            name = f_name + ' ' + l_name
            avatar = obj.avatar
            context = {'name': name, 'avatar': avatar}
    return render(request, 'dashboard/feedback.html', context)'''
