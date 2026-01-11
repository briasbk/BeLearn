from django.db import models
from courses.models import Course
from avatars.models import Avatar

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    CONTENT_TYPES = (
        ('text', 'Text'),
        ('video', 'Video'),
        ('avatar', 'Avatar'),
    )

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    content = models.TextField(blank=True, null=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
