from django.db import models
import uuid
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    roles = models.TextField(max_length=255, null=False)
    intro = models.TextField(max_length=255, null=False)
    image = models.ImageField(upload_to='teranium_project/media', null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    facebook_handle = models.CharField(max_length=100, blank=True, null=True)
    instagram_handle = models.CharField(max_length=100, blank=True, null=True)

class BlogAdmin(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100, null=True)
    categories = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='teranium_project/media', null=True, blank=True)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title