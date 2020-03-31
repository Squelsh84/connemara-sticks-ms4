from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            send_mail(
                'New Contact',
                'You have a new message.',
                'mrmjtwalsh@gmail.com',
                ['mrmjwalsh@gmail.com', ],
                fail_silently=False,
            )
            messages.success(
                request,
                f'Thanks for your message, We will get back soon!'
            )
            return redirect('index')
        else:
            messages.error(request, f'Sorry something went wrong!')
    context = {'title': 'Contact', 'form': form}
    return render(request, 'contact.html', context)
