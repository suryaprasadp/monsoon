from django.conf.urls import url

from . import views

# index-> form is displayed for taking queries and file input
#result->  page which displays queries and option to download csv file generated
#final ->this view lets download when button is pressed



urlpatterns = [
    url(r'^$', views.index, name='index'),          
    url(r'^result/$', views.result, name='result'), 
    url(r'^final/$', views.final, name='final'),]    
