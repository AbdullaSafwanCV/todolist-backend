from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    color_selection = models.CharField(max_length=7, default='#FF5733')  # Default color, can be changed
    
    def __str__(self):
        return self.name

class AddNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    tags = models.ManyToManyField(Tags, related_name='notes', blank=True)
    title = models.CharField(max_length=512)
    content = models.TextField()
    duedate = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return str(self.id)




