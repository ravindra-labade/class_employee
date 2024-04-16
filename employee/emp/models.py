from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=20)
    emp_sal = models.IntegerField()
    company_name = models.CharField(max_length=20)
    choice = [('WFH', 'Work From Home'), ('WFO', 'Work From Office')]
    work_mode = models.CharField(max_length=10, choices=choice)

