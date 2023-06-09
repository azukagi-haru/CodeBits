from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Code(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    snippet = models.TextField(default=None, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('codeapp-code-detail', kwargs={'pk': self.pk})

class Folder(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('codeapp-code-detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    code_origin = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='comments')    
    
    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('code-detail', kwargs={'pk': self.code_origin.pk})

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    comment_origin = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    
    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('code-detail', kwargs={'pk': self.code_origin.pk})