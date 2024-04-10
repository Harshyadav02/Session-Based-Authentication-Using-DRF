from django.db import models

class Employee(models.Model) :
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=10)
    employee_age = models.IntegerField(null=True)
    employee_salary = models.FloatField()

