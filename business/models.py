import uuid
from django.db import models


class Business(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    social_name = models.CharField(max_length=500)
    nif = models.CharField(max_length=15)
    phone = models.CharField(max_length=15,default=True)
    is_active = models.CharField(max_length=20,default=True,null=False)
    address = models.CharField(max_length=255,default=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'businesses'
        
    def __str__(self):
        return self.social_name
    