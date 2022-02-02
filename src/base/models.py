from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'C-{self.name.title()}'

class Task(models.Model):
    STATUS_CHOINES = (
        ('All', 'All'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Close', 'Close')        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    comments = models.CharField(max_length=30)
    state  = models.CharField('State', max_length=20, choices=STATUS_CHOINES, 
                                default='A')
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)                         
    expire_date = models.DateTimeField('Expired Date ', null=True, blank=True)

    class Meta:
        ordering = ['expire_date']

    def __str__(self):
        return self.name
        return datetime.today() > self.date.replace(tzinfo=None)
    

    
    