from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Location, Bank, Developer


# Create your views here.
def home(request):
    context = {
        'for_sale': Property.objects.all().filter(status=True),
        'for_rent': Property.objects.all().filter(status=False),
        'featured': Property.objects.all().filter(featured=True),
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types()
    }
    return render(request, 'GoldMark/home.html', context=context)


def view_property(request):
    unit_id = int(request.GET['id'])
    unit = Property.objects.get(pk=unit_id)
    context = {
        'unit': Property.objects.get(pk=unit_id),
        'banks': Bank.objects.all(),
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types()
    }
    return render(request, 'GoldMark/viewproperty.html', context=context)


def process_message(request):
    return HttpResponse("hello")


def search_properties(requests):
    if len(requests.GET) == 0:
        return render(requests, 'GoldMark/searchresults.html', context={
            'locations': Location.objects.all(),
            'developers': Developer.objects.all(),
            'types': Property.get_types(),
            'has_result': False})
    result = Location.objects.all()
    indexes = requests.GET
    if 'location' in indexes.keys():
        locations = requests.GET.getlist('location')
        result = Location.objects.all().filter(name__in=locations)
    properties = Property.objects.all().filter(location__in=result)
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
    context = {
        'results': properties,
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'has_result': True
    }
    return render(requests, 'GoldMark/searchresults.html', context=context)


