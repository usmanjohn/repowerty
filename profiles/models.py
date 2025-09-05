from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    GENDER = (
    ("male", "Male"),
    ("female", "Female"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.CharField(max_length = 1200)
    gender = models.CharField(max_length = 7, choices = GENDER, default = 'female')
    is_member = models.BooleanField(default = False)
    is_supermember = models.BooleanField(default = False)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add = True)
    
    @property
    def telegram_url(self):
        if self.telegram_username:
            return f'https://t.me/{self.telegram_username}'
        return None
    def __str__(self):
        return self.user.username