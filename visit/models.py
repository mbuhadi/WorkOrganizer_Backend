from django.db import models
from employee.models import Employee
from school.models import School

class ReturnTime(models.Model):
    times = models.CharField(
        max_length=40,
        default='02:00 PM',
        primary_key=True,
        unique=True,
        db_index=True)
    def __str__(self):
        return self.times

class Visit(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.DO_NOTHING,

    )
    date_time_Current = models.DateTimeField(auto_now_add=True)
    time_Of_return = models.ForeignKey(
        ReturnTime,
        on_delete=models.DO_NOTHING,
    )
    schools = models.ForeignKey(
        School,on_delete=models.DO_NOTHING,
        related_name="schools",
    )

    def __str__(self):
        return str(self.employee)