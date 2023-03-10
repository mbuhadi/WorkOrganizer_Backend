from django.db import models

class Degree(models.Model):

    name_ar = models.CharField(max_length=40)
    name_en = models.CharField(
        max_length=40,
        primary_key=True,
        unique=True,
        db_index=True)

    def __str__(self):
        return self.name_ar



class SubDepartment(models.Model):
    name_ar = models.CharField(max_length=40)
    name_en = models.CharField(
        max_length=40,
        primary_key=True,
        unique=True,
        db_index=True)

    def __str__(self):
        return self.name_ar
    


class Employee(models.Model):

    name_ar = models.CharField(max_length=40)
    name_en = models.CharField(max_length=40)
    national_id = models.CharField(
        max_length=12,
        primary_key=True,
        unique=True,
        db_index=True,
    )
    file_number = models.CharField(
        max_length=6,
    )
    degree = models.ForeignKey(
        Degree,
        on_delete=models.RESTRICT,
        related_name="degree"
    )
    sub_department = models.ForeignKey(
        SubDepartment,
        on_delete=models.RESTRICT, 
        related_name="occupation_name"
    )

    def __str__(self):
        return self.name_en
    

