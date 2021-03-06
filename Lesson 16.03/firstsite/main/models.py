from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson_title = models.CharField(max_length = 200)
    lesson_materials = models.TextField()
    lesson_time = models.DateTimeField("started time")

    def __str__(self):
        return self.lesson_title