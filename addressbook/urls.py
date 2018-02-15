from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.address_list, name='address_list'),
]
