from django.db import models


class Job(models.Model):
    """ Database for completed projects"""
    image = models.ImageField(upload_to='job_images')
    summary = models.CharField(max_length=257)
