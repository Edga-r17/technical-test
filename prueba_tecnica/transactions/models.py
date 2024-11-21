from django.db import models

# Create your models here.
class RawTransaction(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=130, null=True)
    company_id = models.CharField(max_length=50, null=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    status = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(null=True)
    paid_at = models.DateTimeField(null=True, blank=True)


class Company(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=130, null=True)

class Charge(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=False)
    status = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, blank=True)
