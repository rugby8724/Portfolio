from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=177, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    blog_body = models.TextField(max_length=557, default='Add Blog Description Here')
    image = models.ImageField(upload_to='blog_images')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
