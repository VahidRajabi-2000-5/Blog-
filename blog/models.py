from django.db import models
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = [
        ("pub", "Published"),
        ("drf", "Draft"),
    ]

    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    
    def get_absolute_url(self):
        # return reverse("post_detail", kwargs={"pk": self.pk})
        return reverse("post_detail", args=[self.id])
    
    
    def __str__(self):
        return self.title
