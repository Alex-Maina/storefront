from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)
    
class TaggedItem(models.Model):
    #tag to be applied to an object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #type of object
    #ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()