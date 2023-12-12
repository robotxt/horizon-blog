import uuid
from django.db import models


class BaseDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateField(null=True)

    class Meta:
        abstract = True


class Blog(BaseDateModel):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_date = models.DateTimeField(null=True)
