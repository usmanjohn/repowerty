from django.contrib import admin
from .models import Practice, PracitceQuestions, PracticeAttempt, UserPrAnswer 
admin.site.register([Practice, PracitceQuestions, PracticeAttempt, UserPrAnswer])
# Register your models here.
