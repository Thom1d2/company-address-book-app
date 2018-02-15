from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    manager = models.CharField(max_length=200, default='Adam')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    address = models.TextField()
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)


    def publish(self):
        self.save()

    def __str__(self):
        return self.name


'''
class Manager(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="manager",
    )
'''
