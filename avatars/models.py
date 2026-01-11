from django.db import models

class Avatar(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    voice = models.CharField(max_length=50)
    language = models.CharField(max_length=10, default='en')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AvatarSession(models.Model):
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
