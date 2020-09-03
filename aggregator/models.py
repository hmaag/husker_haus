from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    # come back and set the defaults -> probably should be CASCADE
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.SET_NULL) # recursive relationship here
    content = models.TextField() # do we need a max_length?
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user))