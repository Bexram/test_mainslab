from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Org(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    clorgid = models.FloatField()
    sum = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.client.name} {self.date}'
