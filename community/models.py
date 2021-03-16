from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Fiction(models.Model):
    fiction_subject = models.CharField(max_length=100)
    fiction_text = models.TextField()
    create_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_time = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.fiction_subject

class Comment(models.Model):
    fiction = models.ForeignKey(Fiction, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_time = models.DateTimeField(null=True, blank=True)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField(null=True, blank=True)
    reply_text = models.TextField()
