from django.contrib import admin
from .models import Contact, SMSMessage, SMS

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_phone_numbers', 'get_last_message')

    def get_phone_numbers(self, obj):
        # دریافت شماره‌های ثبت شده توسط کاربر
        contacts = Contact.objects.filter(user=obj.user)
        # ایجاد یک لیست از شماره‌ها با جداکننده "،"
        return "، ".join([contact.phone_number for contact in contacts])

    get_phone_numbers.short_description = 'شماره‌ها'

    def get_last_message(self, obj):
        # دریافت آخرین پیام ارسال شده توسط کاربر
        last_sms = SMSMessage.objects.filter(user=obj.user).order_by('-created_at').first()
        return last_sms.message if last_sms else 'ندارد'

    get_last_message.short_description = 'آخرین پیام'

# ثبت مدل Contact در پنل ادمین
admin.site.register(Contact, ContactAdmin)
admin.site.register(SMSMessage)
admin.site.register(SMS)
