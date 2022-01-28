from django.db import models
from django.contrib.auth.models import User

class BOS_topic(models.Model):
    """Create a topic or risk for entry into BOS's"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'BOS topics'

    def __str__(self):
        """Return string representation of model"""
        return self.text

class BOS_shift(models.Model):
    """Create a Shift for entry into BOS's"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'BOS shifts'

    def __str__(self):
        """Return string representation of model"""
        return self.text

class BOS_area(models.Model):
    """Create an area for entry into BOS's"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'BOS Areas'

    def __str__(self):
        """Return string representation of model"""
        return self.text

class BOS(models.Model):
    """The main structure of a BOS"""
    
    Area = models.ForeignKey(BOS_area, on_delete=models.CASCADE)
    Shift = models.ForeignKey(BOS_shift, on_delete=models.CASCADE)
    Topic = models.ForeignKey(BOS_topic, on_delete=models.CASCADE)
    Comments = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'BOS Entries'

    def __str__(self):
        ID = str(self.id)
        return ('BOS #' + ID)
