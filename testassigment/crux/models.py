from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.data_type})"


class Record(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=20)
    score = models.CharField(max_length=100)
    grade = models.CharField(max_length=1)

    def __str__(self):
        return self.name

