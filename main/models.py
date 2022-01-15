from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    slug = models.SlugField()
    content = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.content

class Choice(models.Model):
    choice = models.CharField(max_length=1024)
    question = models.ForeignKey('Question' , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{}-{}'.format(self.question.content[:10] , self.choice)


class Answer(models.Model):
    question = models.ForeignKey('Question' , on_delete=models.CASCADE)
    choice  = models.ForeignKey('Choice' , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)