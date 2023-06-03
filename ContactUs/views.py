from django.shortcuts import render
from PropertyMarket.models import Property, Location, Developer
from .forms import SendMessageForm
from django.http import HttpResponse, HttpResponseBadRequest
from .models import ContactMessage
from FAQS.models import FaqCategory

# Create your views here.
def contact_us(requests):
    context = {
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'categories': FaqCategory.objects.all(),
        'contact': SendMessageForm()
    }
    return render(requests, 'ContactUs/contact.html', context=context)



def submitContactForm(request):
    # Validate CSRF token
    if not request.POST.get('csrfmiddlewaretoken'):
        return HttpResponseBadRequest('Missing CSRF token')
    form = SendMessageForm(request.POST)
    if form.is_valid() == False:
        return HttpResponseBadRequest("Form Corrupted")
    contactData = form.data
    name = contactData["name"]
    email = contactData["email"]
    phoneNumber = contactData["phonenumber"]
    message = contactData["message"]
    contactMessage = ContactMessage(name=name, 
                                    email=email, 
                                    phoneNumber=phoneNumber,
                                    message=message)
    contactMessage.save()
    return HttpResponse("Request Submitted Successfully")