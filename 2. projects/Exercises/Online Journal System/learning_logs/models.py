from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200) # CharField - small amount of data that's made up of characters, or text.
    date_added = models.DateTimeField(auto_now_add=True) # DateTimeField - a piece of data will record a date and time.
    # auto_now_add=True - to automatically set this attribute to the current date and time.

    def __str__(self):
        """Return a string representation of the model."""
        return self.text