from django.shortcuts import render
from PropertyMarket.models import Location, Developer, Property
from .models import FaqCategory, Faq

# Create your views here.
def view_faqs(requests):
    context = {
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'categories': FaqCategory.objects.all(),
        'FAQS': Faq.objects.all(),
        'featured': Property.objects.all().filter(featured=True)[0:3]
    }
    return render(requests, 'FAQS/FAQS.html', context=context)