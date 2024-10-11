from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name}: {self.phone_number}"

class SMSMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # کاربری که پیامک را ارسال کرده
    message = models.TextField()  # محتوای پیامک
    all_customers = models.BooleanField(default=False)  # آیا برای همه مشتریان ارسال شده؟
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ارسال

    def __str__(self):
        return f"پیامک از {self.user.username} - {self.created_at}"

class SMS(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message