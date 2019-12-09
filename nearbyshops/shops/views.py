from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = -74.005974
latitude = 40.712776

#this ideally should be specified by the user or retrieved automatically from the user’s browser with their permission using JavaScript and the HTML5 GeoLocation API
user_location = Point(longitude, latitude, srid=4326)

#Class-based views: alternative to functions as a way to implement views in Python/Django
class Home(generic.ListView): # by sub-classing the ListView generic view and overridding the model, context_object_name, queryset, and template_name attributes, the list view now handles HTTP requests without any extra code
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location) #annotate each object on the returned queryset with a distance annotation that’s calculated using Distance(), available from GeoDjango, between the location of each shop and the user’s location
    ).order_by('distance')[0:6] #order the returned queryset by the distance annotation and take only the nearest six shops
    template_name = 'shops/index.html'