from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name='Location name')
    latitude = models.IntegerField(default=0, verbose_name='latitude coordinates')
    longitude = models.IntegerField(default=0, verbose_name='longitude coordinates')

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Agency name')
    email = models.EmailField(verbose_name='Agency email')
    headquarters = models.CharField(max_length=100, verbose_name='Agency head quarters')
    phone = models.CharField(max_length=20, verbose_name='Agency phone number')
    image = models.ImageField(upload_to='propertyMarket/images/Agencies/profiles/', verbose_name='Agency logo',
                              blank=True, null=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    Agency = models.ForeignKey(Developer, on_delete=models.CASCADE,
                               blank=True, null=True, verbose_name='Agency the agent belongs to')
    User = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='the user name')

    def __str__(self):
        return "Agent " + self.User.username


class Property(models.Model):
    name = models.CharField(max_length=100, verbose_name='Property name')
    status = models.BooleanField(verbose_name='Status',
                                 choices={
                                     (True, 'For sale'),
                                     (False, 'For rent')
                                 })
    featured = models.BooleanField(verbose_name='Featured', default=False)
    price = models.IntegerField(verbose_name='property price')
    features = models.JSONField(verbose_name='property features', default=dict,
                                blank=True, null=True)
    info = models.JSONField(default=dict, verbose_name='additional info as json string',
                            blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='property address')
    latitude = models.FloatField(default=0, verbose_name='google latitude')
    longitude = models.FloatField(default=0, verbose_name='google longitude')
    video = models.FileField(upload_to='propertyMarket/images/properties/videos/', verbose_name='property video',
                             blank=True, null=True)
    time_posted = models.DateTimeField(default=timezone.now, verbose_name='time posted')
    size = models.IntegerField(verbose_name='property lot size')
    description = models.CharField(max_length=500, verbose_name='property description')
    plan = models.ImageField(upload_to='propertyMarket/images/properties/plans/',
                             verbose_name='property plan view', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='Location')
    area = models.IntegerField(verbose_name='Property total area')
    Developer = models.ForeignKey(Developer, on_delete=models.CASCADE,
                                  blank=True, null=True, verbose_name='Development group')
    bedrooms = models.IntegerField(verbose_name='Number of bedrooms', null=True, blank=True)
    bathrooms = models.IntegerField(verbose_name='Number of bathrooms', null=True, blank=True)
    image = models.ImageField(upload_to='propertyMarket/images/properties/residential/profiles',
                              verbose_name='profile image')
    garage = models.IntegerField(verbose_name='number of garage places', null=True, blank=True)
    type = models.CharField(max_length=100, verbose_name='Property Type',
                            choices={
                                ("town house", "town house"),
                                ("apartment", "apartment"),
                                ("villa", "villa"),
                                ("twin house", "twin house"),
                                ("chalet", "chalet"),
                                ("duplex", "duplex"),
                                ("pent house", "pent house"),
                                ("serviced apartment", "serviced apartment"),
                                ("studio", "studio"),
                                ("office", "office"),
                                ("restaurant", "restaurant"),
                                ("retail", "retail"),
                                ("Industrial", "Industrial"),
                                ("clinic", "clinic")
                            })
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name='Property it belongs to')

    def __str__(self):
        return self.name + " " + str(self.id)

    def is_compound(self):
        return len(self.propertyimage_set.all()) != 0

    def get_images(self):
        return list(map(lambda x: x.image, self.propertyimage_set.all()))


class PropertyImage(models.Model):
    image = models.ImageField(upload_to='propertyMarket/images/properties/residential/', verbose_name='Image location')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='Property it belongs to')

    def __str__(self):
        return "Image " + str(self.id)


class Bank(models.Model):
    name = models.CharField(max_length=50, verbose_name='Bank name')
    office = models.CharField(max_length=100, verbose_name='Office address')
    number = models.CharField(max_length=20, verbose_name='Number')
    hotline = models.CharField(max_length=10, verbose_name='Hotline', blank=True, null=True)
    email = models.EmailField(verbose_name='Bank email')
    website = models.URLField(verbose_name='Website link')
    image = models.ImageField(upload_to='propertyMarket/images/banks/profiles/', verbose_name='Bank image')
    interest = models.FloatField(verbose_name='Bank interest rate')

    def __str__(self):
        return self.name
