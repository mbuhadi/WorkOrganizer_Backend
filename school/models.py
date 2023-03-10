from django.db import models


class Area(models.Model):

    name_ar = models.CharField(max_length=40)
    name_en = models.CharField(
        max_length=40,
        primary_key=True,
        unique=True,
        db_index=True)

    def __str__(self):
        return self.name_ar


class School(models.Model):
    name_en = models.CharField(
        max_length=60,
        primary_key=True,
        unique=True,
        db_index=True)
    name_ar = models.CharField(max_length=60)

    area = models.ForeignKey(
        Area, on_delete=models.RESTRICT, related_name="school_area"
    )

    def __str__(self):
        return self.name_ar