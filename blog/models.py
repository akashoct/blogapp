from django.db import models
from django.utils import timezone  # set the date when object is created
from django.contrib.auth.models import User
from django.urls import reverse
# separate user model like one to many relationship like one author
# can have multiple post but but one post can have only one author so for that we can use foreign key NOW WE MAKE
# CHANGES INTO DATABASE USING MIGRATE COMMAND


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Second argument telling django that if user is deleted so its post is also going to be deleted but only one way

    def __str__(self):
        return self.title

    """
    we are creating this function so that after creating new post it can redirect back 
    to the url we are going to provide in the function 
    we cannot use redirect just like we using before because redirect 
    and reverse work differently and reverse requires view name ]
    and primary key
    """
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



