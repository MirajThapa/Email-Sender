from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

# Create your own Views
def email_sent_success(request):
    return render(request, 'app/success.html')

def email_sender(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient', '')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        attachment = request.FILES.get('attachment')
        
        mail = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[recipient])
        if attachment:
            mail.attach(attachment.name,attachment.read(),attachment.content_type)

        else:
            print("null")

        mail.send()
        return HttpResponseRedirect(reverse('email_sent_success'))

    return render(request, "app/index.html", {"title":"Email Sender App"})
