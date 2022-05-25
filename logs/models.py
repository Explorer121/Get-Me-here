from django.db import models

# Create your models here.
class Whatsapp(models.Model):
    Whatsapp = models.CharField(max_length=122)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Whatsapp