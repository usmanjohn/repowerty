from django.db import models
import datetime
from django.contrib.auth.models import User
import skills.models as skill_models

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'experience')
    workplace = models.CharField(max_length = 150, blank = True, null = True)
    workplace_description = models.TextField(null = True, blank = True )
    country = models.CharField(max_length = 150, blank = True, null = True)
    city = models.CharField(max_length = 150, blank = True, null = True)
    branch = models.CharField(max_length = 150, null = True, blank = True)
    department = models.CharField(max_length = 150, null = True, blank = True)
    position = models.CharField(max_length = 150, null = True, blank = True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    responsibility = models.TextField(null = True, blank = True)
    skills = models.ManyToManyField(skill_models.Skills, blank = True)
    languages = models.ManyToManyField(skill_models.Languages, blank = True)
    achievements = models.TextField(null = True, blank = True)
    workplace_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    workplace_avatar = models.ImageField(default='default.jpg', upload_to='workplace')
    
    def __str__(self):
        return f"{self.user.username}'s work at {str(self.workplace)[:10]}"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'education')
    institute = models.CharField(max_length = 150, blank = True, null = True)
    institute_description = models.TextField(null = True, blank = True )
    country = models.CharField(max_length = 150, blank = True, null = True)
    city = models.CharField(max_length = 150, blank = True, null = True)
    level = models.CharField(max_length = 150, blank = True, null = True)
    major = models.CharField(max_length = 150, null = True, blank = True)
    skills = models.ManyToManyField(skill_models.Skills, blank = True)
    languages = models.ManyToManyField(skill_models.Languages, blank = True)
    
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    gpa = models.FloatField(null=True, blank=True, default=0.0)
    max_gpa = models.FloatField(null=True, blank=True, default=0.0)
    projects = models.TextField(null = True, blank = True)
    focus = models.TextField(null = True, blank = True)
    achievements = models.TextField(null = True, blank = True)
    institute_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    institute_avatar = models.ImageField(default='default.jpg', upload_to='institute')
    
    def __str__(self):
        return f"{self.user.username}'s work at {str(self.institute)[:10]}"


class Internship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'internship')
    organization = models.CharField(max_length = 150, blank = True, null = True)
    organization_description = models.TextField(null = True, blank = True )
    country = models.CharField(max_length = 150, blank = True, null = True)
    city = models.CharField(max_length = 150, blank = True, null = True)
    branch = models.CharField(max_length = 150, null = True, blank = True )
    department = models.CharField(max_length = 150, null = True, blank = True)
    position = models.CharField(max_length = 150, null = True, blank = True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    responsibility = models.TextField(null = True, blank = True)
    skills = models.ManyToManyField(skill_models.Skills, blank = True)
    languages = models.ManyToManyField(skill_models.Languages, blank = True)
    grants = models.ManyToManyField(skill_models.Grants, blank = True)
    
    achievements = models.TextField(null = True, blank = True)
    organization_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)    
    internship_avatar = models.ImageField(default='default.jpg', upload_to='internship')
    
    def __str__(self):
        return f"{self.user.username}'s work at {str(self.organization)[:10]}"
