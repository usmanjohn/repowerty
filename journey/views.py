from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Experience, Education, Internship
def journey_home(request):
    user = User.objects.get(username = 'powerty')
    print(user)
    experiences = Experience.objects.filter(user = user)
    print(experiences)
    educations = Education.objects.filter(user = user)
    print(educations)
    internships = Internship.objects.filter(user = user)
    context = {'user':user, 'experiences':experiences, 'educations':educations, 'internships':internships}
    return render(request, 'journey/home.html', context)
# Create your views here.
