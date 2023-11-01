from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):
    # ... other fields ...

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='customuser_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_permissions',
    )

    

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
