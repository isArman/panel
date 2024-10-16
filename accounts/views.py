from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import SMSMessage

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # رمز عبور را به صورت هش شده ذخیره کنید
            user.save()
            messages.success(request, 'حساب با موفقیت ساخته شد!')
            return redirect('login')  # کاربر را به صفحه لاگین هدایت کنید
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # به صفحه خانگی بروید
            else:
                messages.error(request, 'نام کاربری یا رمز عبور نادرست است.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    contacts = Contact.objects.filter(user=request.user)
    #contacts = Contact.objects.all()  # دریافت تمام شماره‌ها
    return render(request, 'accounts/home.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            #form.save()  # ذخیره‌سازی در دیتابیس
            return redirect('view_contacts')  # هدایت به صفحه اصلی
        else:
            print(form.errors)
    else:
        form = ContactForm()
    return render(request, 'accounts/add_contact.html', {'form': form})

def view_contacts(request):
    contacts = Contact.objects.filter(user=request.user)  # فیلتر بر اساس کاربر جاری
    # کد برای نمایش تماس‌ها
    return render(request, 'accounts/view_contacts.html', {'contacts': contacts})

def logout_view(request):
    logout(request)
    return redirect('login')

# def send_sms(request):
#     if request.method == 'POST':
#         # منطق ارسال پیامک را اینجا اضافه کن
#         send_to_all = request.POST.get('send_to_all', False)
#         if send_to_all:
#             # ارسال پیامک به همه مشتریان
#             pass
#         return render(request, 'accounts/send_sms.html')  # صفحه‌ای که بعد از ارسال نمایش داده می‌شود
#     return render(request, 'accounts/send_sms.html')

def send_sms(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        all_customers = request.POST.get('all_customers') == 'on'  # چک‌باکس بررسی می‌شود
        
        # ذخیره پیامک در دیتابیس
        sms = SMSMessage.objects.create(
            user=request.user,
            message=message,
            all_customers=all_customers
        )
        
        # نمایش پیام موفقیت‌آمیز
        messages.success(request, "پیامک با موفقیت ارسال شد!")
        return redirect('home')

    return render(request, 'accounts/send_sms.html')