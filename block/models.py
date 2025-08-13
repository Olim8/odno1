from django.db import models

class UserCredential(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)  # bu yerda hashlangan parol saqlanadi
    # photo=models.ImageField(upload_to='img')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username