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

class Teacher(models.Model):
    NIVEL_CHOICES = [
        ("anteprescolar", "Antepreșcolar"),
        ("prescolar", "Preșcolar"),
        ("primar", "Primar"),
        ("gimnazial", "Gimnazial"),
        ("liceal", "Liceal"),
    ]

    name = models.CharField(max_length=160)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "nivel")

    def __str__(self):
        return f"{self.name} ({self.nivel})"


class SchoolClass(models.Model):
    name = models.CharField(max_length=50)  # pl. "V A"
    nivel = models.CharField(max_length=20, choices=Teacher.NIVEL_CHOICES)
    clasa = models.PositiveIntegerField()  # évfolyam: 0..12
    litera = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        ordering = ["nivel", "clasa", "litera"]
        unique_together = ("nivel", "clasa", "litera")

    def __str__(self):
        return f"{self.nivel} - Clasa {self.clasa}{self.litera or ''}"


class PlanRow(models.Model):
    nivel = models.CharField(max_length=20, choices=Teacher.NIVEL_CHOICES)
    profil = models.CharField(max_length=120, blank=True, null=True)
    clasa = models.PositiveIntegerField()
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    ore = models.PositiveIntegerField()

    class Meta:
        ordering = ["area__order", "subject__name"]
        unique_together = ("nivel", "profil", "clasa", "area", "subject")

    def __str__(self):
        return f"{self.nivel} cl.{self.clasa} {self.subject.name} ({self.ore}h)"
