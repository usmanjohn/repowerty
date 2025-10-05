from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Skills(models.Model):
    Category_CHOICES = (
    ('coding','Coding'),
    ('soft', 'Soft'),
    ('hard','Hard'),
    ('other','Other'))
    Progress_CHOICES = (
    ('advanced','Advanced'),
    ('intermediate', 'Intermediate'),
    ('average','Average'),
    ('beginner','Beginner'),
    ('beginner','Beginner'),)
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'skills')
    name = models.CharField(max_length = 150, null = False, blank = False)
    category = models.CharField(max_length = 20, choices = Category_CHOICES, default = 'other')
    description = models.TextField(blank = True, null = True)
    skilled_date = models.DateField(default = timezone.now) 
    progress = models.CharField(max_length = 20, choices = Progress_CHOICES, default = 'average')
    link = models.URLField(blank = True, null = True)
    def __str__(self):
        return f"{self.user.username}'s skill => {str(self.name)[:10]}"



class Certificates(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'certificates')
    name = models.CharField(max_length = 150, null = False, blank = False)
    given_by = models.CharField(max_length = 150, null = False, blank = False)
    given_at = models.DateField(default = timezone.now)
    has_deadline = models.BooleanField()
    expire_at = models.DateField(default = timezone.now)
    score = models.FloatField(null=True, blank=True, default=0.0)
    max_score = models.FloatField(null=True, blank=True, default=0.0)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(default='default.jpg', upload_to='certificates')
    link = models.URLField(blank = True, null = True)
    
    def __str__(self):
        return f"{self.user.username}'s certfct => {str(self.name)[:10]}"
    
class Languages(models.Model):
    language_CHOICES = (
    ('advanced','Advanced'),
    ('intermediate', 'Intermediate'),
    ('medium','medium'),
    ('beginner','beginner'))
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'languages')
    name = models.CharField(max_length = 150, null = False, blank = False)
    
    reading = models.CharField(max_length = 150, choices = language_CHOICES, default = 'intermediate')
    speaking = models.CharField(max_length = 150, choices = language_CHOICES, default = 'intermediate')
    listening = models.CharField(max_length = 150, choices = language_CHOICES, default = 'intermediate')
    writing = models.CharField(max_length = 150, choices = language_CHOICES, default = 'intermediate')
    certificate = models.ForeignKey(Certificates, on_delete = models.SET_NULL, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    know_from = models.DateField(default = timezone.now)
    def __str__(self):
        return f"{self.user.username}'s certfct => {str(self.name)[:10]}"
           


class Grants(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'grants')
    name = models.CharField(max_length = 150, null = False, blank = False)
    organisation = models.CharField(max_length = 150, null = False, blank = False)
    org_country = models.CharField(max_length = 150, null = False, blank = False)
    purpose = models.CharField(max_length = 150, null = False, blank = False)
    given_by = models.CharField(max_length = 150, null = False, blank = False)
    given_at = models.DateField(default = timezone.now)
    has_deadline = models.BooleanField()
    expire_at = models.DateField(default = timezone.now)
    amount = models.FloatField(blank = True, null = True, default = 0.0)
    image = models.ImageField(default='default.jpg', upload_to='certificates')
    link = models.URLField(blank = True, null = True)
    
    def __str__(self):
        return f"{self.user.username}'s certfct => {str(self.name)[:10]}"
    