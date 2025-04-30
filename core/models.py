import uuid
from django.db import models
from django.utils import timezone

class SharedFile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    file = models.FileField(upload_to='uploads/')  
    password = models.CharField(max_length=255, blank=True, null=True) 
    expiry = models.DateTimeField(blank=True, null=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True) 

    def is_expired(self):
        return self.expiry and timezone.now() > self.expiry

    def __str__(self):
        return f"File: {self.file.name}, Expiry: {self.expiry}"
