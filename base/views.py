from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from base.data import CERTIFICATIONS
from base.forms import Contact
from django.core.mail import send_mail

def home(request):              
    if request.method == 'POST':
        contact = Contact(request.POST)
        if contact.is_valid():
            info_contact = contact.cleaned_data
            #send message
            html_content = render_to_string('base/email.html')
            msg = EmailMessage(info_contact["subject"], html_content, "manuelgilsitio@gmail.com",[info_contact["email"]])
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
        
            message = "sucess"
        else:
            message = "failed"

        return redirect("contact",message=message)
    return render(request, "base/index.html")

def all_certifications(request):
    return render(request, 'base/all_certifications.html', {"certifications":CERTIFICATIONS})

def contact(request,message):
    return render(request,"base/contact.html",{"message":message})

        