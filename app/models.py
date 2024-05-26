from django.db import models


# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=123,primary_key=True)
    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=123)
    url=models.URLField()
    email=models.EmailField()
    def __str__(self):
        return (self.name)


class AccessRecord(models.Model):
     name=models.ForeignKey(webpage,on_delete=models.CASCADE)
     date=models.DateField()
     author=models.CharField(max_length=34)

     def __str__(self):
        return self.author
