from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import *
from django.conf import settings
from django.contrib import messages
from .models import *
from django.core.mail import send_mail


def index(request):
    return render(request, 'hello/index.html')


def about(request):
    return render(request, 'hello/about.html')


def register(request):
    return render(request, 'hello/register.html')


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except:
                form.add_error(None, 'Мақаланы қосқанда қате шықты.')
    else:
        form = AddPostForm()
    return render(request, 'hello/addpage.html', {'title':'Мақаланы қосу', 'form': form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'hello/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title='Registration')
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'hello/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title="Login")
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass

    def get_success_url(self):
        return reverse_lazy('/')


def logout_user(request):
    logout(request)
    return redirect('login')


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'hello/susccesfull.html'

    def get(self, request):
        form = self.form_class()
        return render(request,'hello/succesfull.html',{'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'hello/succesfull.html',
                              {'email_form': form, 'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'hello/succesfull.html',
                              {'email_form': form, 'error_message': 'Tіркеме тым үлкен немесе бүлінген'})

        return render(request, 'hello/succesfull.html',
                      {'email_form': form, 'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})