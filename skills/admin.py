from django.contrib import admin
from .models import Skills, Languages,Certificates, Grants

admin.site.register([Skills, Languages,Certificates, Grants])
# Register your models here.
