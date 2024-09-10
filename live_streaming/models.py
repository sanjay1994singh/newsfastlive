from django.db import models


# Create your models here.
class LiveStreaming(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'live_streaming'
