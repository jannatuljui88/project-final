from django.db import models

class Deposite (models.Model):
    Date = models.CharField(max_length=200)
    Amount = models.IntegerField()

class Loan(models.Model):
     Date = models.ForeignKey(Deposite, on_delete =models.CASCADE)
     Amount = models.IntegerField()

class Transfer(models.Model):
    Date = models.ForeignKey(Deposite,on_delete=models.CASCADE)
    Amount = models.IntegerField()