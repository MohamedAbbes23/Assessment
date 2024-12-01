from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('error', 'Error'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)      
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    
    def __str__(self):
        return self.name
