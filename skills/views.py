from django.shortcuts import render
def skills_home(request):
    return render(request, 'skills/home.html')