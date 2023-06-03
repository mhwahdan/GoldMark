from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Contactor name')
    email = models.EmailField(max_length=100, verbose_name="email address", unique=False)
    phoneNumber = models.CharField(max_length=20, verbose_name='Phone number')
    message = models.CharField(max_length=250, verbose_name='Message content')
    
    def __str__(self):
        return self.name

    def get_messages(self):
        return self.message_set.all()
