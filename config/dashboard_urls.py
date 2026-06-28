from django.shortcuts import render
from django.urls import path
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def attendance(request):
    return render(request, 'attendance/record_list.html')


@login_required
def history(request):
    return render(request, 'dashboard/history.html')


@login_required
def profile(request):
    return render(request, 'profile/view.html')


urlpatterns = [
    path('', home, name='home'),
    path('presencas/', attendance, name='attendance'),
    path('historico/', history, name='history'),
    path('perfil/', profile, name='profile'),
]
