from django.db import models
from django.utils.safestring import mark_safe


class Project(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    date = models.DateField(verbose_name="Date", auto_now=False, auto_now_add=False)
    image = models.ImageField(verbose_name="Image", upload_to="portfolio-images")
    
    def __str__(self):
        return self.title
    def get_image(self):
            if self.image:
                return mark_safe(f'<img src="{self.image.url}" alt="{self.title}" width="100" height="100" />')
            else:
                return mark_safe('<img src="data:image/png;base64,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"/>')
    get_image.short_description = "picture"

class Contact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200,  null=True, blank=True)
    email = models.EmailField(verbose_name="Email",  null=True, blank=True)
    subject = models.CharField(verbose_name="Subject", max_length=200)
    message = models.TextField(verbose_name="Message")
    
    def __str__(self):
        return self.name

    