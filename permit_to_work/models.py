from django.db import models
from bos.models import Area

class permit_to_work(models.Model):
    """Basic ptw structure"""
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Permit to work'
        verbose_name_plural = 'Permits to work'

    def __str__(self):
        return ('PTW #' + str(self.id))