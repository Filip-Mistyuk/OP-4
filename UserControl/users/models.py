from django.db import models

# Create your models here.

class User(models.Model):
    class Role(models.TextChoices):
        admin = "admin", "ADMIN"
        user = "user", "USER"

    login = models.CharField(max_length=63, unique=True)
    email = models.EmailField()
    role = models.CharField(max_length=63, choices=Role.choices, default=Role.user)

    def __str__(self):
        return self.login
    

class Task(models.Model):
    class Status(models.TextChoices):
        done = "done", "DONE"
        process = "processing", "PROCESSING"
        no_work = "no work", "NO WORK"

    status = models.CharField(max_length=63, choices=Status.choices, default=Status.no_work)
    title = models.CharField(max_length = 63)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING, null=True)