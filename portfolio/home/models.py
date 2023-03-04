from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50, unique=True)
    message=models.TextField()
    def __str__(self) -> str:
        return self.name
