from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=255,blank=False)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=False,null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

