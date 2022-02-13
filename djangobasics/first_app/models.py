from django.db import models

# Create your models here.
#model Topic
class Topic(models.Model):
    topic_name = models.CharField(max_length=300,unique=True)

    #string represntaton of the models
    def __str__(self):
        return self.topic_name

# model Webpage
class Webpage(models.Model):
    top_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=300,unique=True)
    url = models.URLField(unique=True)

    #string represntaton of the models
    def __str__(self):
        return self.name

# model AccessRecords
class AccessRecords(models.Model):
    web_name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    create_dt = models.DateField()

    #string represntaton of the models
    def __str__(self):
        return str(self.create_dt)
