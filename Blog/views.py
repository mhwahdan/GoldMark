from django.shortcuts import render
from django.core.paginator import Paginator
from Blog.models import BlogCategory, Blog
from propetyMarket.models import Property, Developer, Location
# Create your views here.


def blogs(requests):
    paginator = Paginator(Blog.objects.all(), 10)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': BlogCategory.objects.all(),
        'Blogs': page_obj,
        'recent': Blog.objects.all()[0:3],
        'featured': Property.objects.all().filter(featured=True)[0:3],
        'types': Property.get_types(),
        'developers': Developer.objects.all()
    }
    return render(requests, 'Blogs/Blogs.html', context=context)


def show_blog(requests):
    blog_id = requests.GET["id"]
    context = {
        'locations': Location.objects.all(),
        'developers': Developer.objects.all(),
        'types': Property.get_types(),
        'blog': Blog.objects.all().get(pk=blog_id),
        'recent': Blog.objects.all().exclude(pk=blog_id)[0:3],
        'categories': BlogCategory.objects.all(),
        'featured': Property.objects.all().filter(featured=True)[0:3]
    }
    return render(requests, 'Blogs/showblog.html', context=context)
