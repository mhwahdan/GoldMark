from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Location, Bank, Developer, FaqCategory, Faq
from . import forms
from django.core.paginator import Paginator
from Blog.models import Blog
# Create your views here.


def home(request):
    for_sale = Property.objects.all().filter(status=True)
    for_rent = Property.objects.all().filter(status=False)
    featured = Property.objects.all().filter(featured=True)
    contactform = forms.SendMessageForm()
    blogs = Blog.objects.all()
    paginator_sale = Paginator(for_sale, 10)
    paginator_rent = Paginator(for_rent, 10)
    blogs_pag = Paginator(blogs, 3)
    page_number_sale = request.GET.get('page_s')
    page_number_rent = request.GET.get('page_r')
    page_number_blog = request.GET.get('page_b')
    page_sale = paginator_sale.get_page(page_number_sale)
    page_rent = paginator_rent.get_page(page_number_rent)
    blogs_out = blogs_pag.get_page(page_number_blog)
    context = {
        'for_sale': page_sale,
        'for_rent': page_rent,
        'featured': featured,
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'blogs': blogs_out,
        'contact_form': contactform
    }
    return render(request, 'GoldMark/home.html', context=context)


def view_property(request):
    unit_id = int(request.GET['id'])
    unit = Property.objects.get(pk=unit_id)
    similar = Property.objects.all().exclude(pk=unit_id)\
        .filter(location=unit.location)\
        .filter(type=unit.type)\
        .filter(status=unit.status)\
        .order_by('featured')[0:5]
    context = {
        'unit': Property.objects.get(pk=unit_id),
        'banks': Bank.objects.all(),
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'similar': similar
    }
    return render(request, 'GoldMark/viewproperty.html', context=context)


def process_message(request):
    return HttpResponse("hello")


def search_properties(requests):
    indexes = requests.GET
    properties = Property.objects.all()
    if 'location' in indexes.keys():
        locations = requests.GET.getlist('location')
        result = Location.objects.all().filter(name__in=locations)
        properties = properties.filter(location__in=result)
    if 'status' in indexes.keys():
        properties = properties.filter(status=(indexes['status'] == 'for-sale'))
    if 'min-price' in indexes.keys():
        properties = properties.filter(price__lte=int(indexes['min-price']))
    if 'max-price' in indexes.keys():
        properties = properties.filter(price__gte=indexes['max-price'])
    if 'min-area' in indexes.keys():
        properties = properties.filter(area__lte=int(indexes['min-area']))
    if 'max-area' in indexes.keys():
        properties = properties.filter(area__gte=int(indexes['max-area']))
    if 'bedrooms' in indexes.keys():
        properties = properties.filter(bedrooms__gte=int(indexes['bedrooms']))
    if 'bathrooms' in indexes.keys():
        properties = properties.filter(bathrooms__gte=int(indexes['bathrooms']))
    if 'type' in indexes.keys():
        types = requests.GET.getlist('type')
        properties = properties.filter(type__in=types)
    paginator = Paginator(properties, 10)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'results': page_obj,
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'has_result': len(properties) != 0
    }
    return render(requests, 'GoldMark/searchresults.html', context=context)


def view_faqs(requests):
    context = {
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'categories': FaqCategory.objects.all(),
        'FAQS': Faq.objects.all(),
        'featured': Property.objects.all().filter(featured=True)[0:3]
    }
    return render(requests, 'GoldMark/FAQS.html', context=context)


def contact_us(requests):
    context = {
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'categories': FaqCategory.objects.all(),
        'contact': forms.SendMessageForm()
    }
    return render(requests, 'GoldMark/contact.html', context=context)




