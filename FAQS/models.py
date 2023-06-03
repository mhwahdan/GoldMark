from django.db import models

# Create your models here.
class FaqCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category name')

    def __str__(self):
        return self.name

    def get_faqs(self):
        return self.faq_set.all()

    def get_class_name(self):
        return self.__str__().replace(' ', '_')


class Faq(models.Model):
    question = models.TextField(verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')
    category = models.ForeignKey(FaqCategory, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.question