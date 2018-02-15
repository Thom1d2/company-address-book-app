from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Person

def address_list(request):
    me = User.objects.get(username='admin')
    address = Person.objects.filter(author=me).order_by('name')
    return render(request, 'addressbook/address_list.html', {'address': address})
