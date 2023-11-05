from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('Not Completed', 'Not Completed'),
        ('Completed', 'Completed'),
    ]
    task_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Not Completed'
    )

    def __str__(self):
        return self.task_name
