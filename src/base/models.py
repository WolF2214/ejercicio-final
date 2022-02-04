from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('All', 'All'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Close', 'Close')        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    comments = models.CharField(max_length=30)
    state  = models.CharField('State', max_length=20, choices=STATUS_CHOICES, 
                                default='A')
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)                         
    expire_date = models.DateTimeField('Expired Date ', null=True, blank=True)
    
    def is_past_due(self):
        return datetime.today() > self.expire_date.replace(tzinfo=None)
    
 