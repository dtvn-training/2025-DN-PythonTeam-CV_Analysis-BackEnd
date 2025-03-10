import uuid
from django.db import models

class JD(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    compulsory = models.JSONField()
    benefits = models.TextField()
    salary = models.IntegerField()
    tag = models.JSONField()
    status = models.BooleanField(default=True)
    user_id = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title