from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=120, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=160, unique=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name="subjects")

    class Meta:
        ordering = ["area__order", "name"]

    def __str__(self):
        return self.name
