from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, "biolog1/index.html")


def about(request):
    return render(request, "biolog1/about.html")


def blog(request):
    return render(request, "biolog1/blog.html")


def contact(request):
    return render(request, "biolog1/contact.html")


def send(request):
    if request.method == 'POST':
        Name = request.POST.get('Name', False)
        Email = request.POST.get('Email', False)
        text = request.POST.get('text', False)

        send_mail(
            Name,
            text,
            Email,
            ['chalukya.reddy.7@gmail.com'],
            fail_silently=False,
        )

        send_mail(
            'WELCOME TO BIOLOG',
            'THANK YOU FOR CONTACTING US',
            Email,
            [Email],
            fail_silently=False,
        )
        return render(request, 'index.html', {'Name': Name})
    else:
        return render(request, 'index.html', {})
