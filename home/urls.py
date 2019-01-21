from django.conf.urls import url
from .views import HomePage


app_name = 'home'


urlpatterns = [

    url(r'^$', HomePage.as_view(), name='home'),

]
