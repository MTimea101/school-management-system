from django.db import models
from django.core.exceptions import ValidationError


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


class Allocation(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, related_name='allocations')
    school_class = models.ForeignKey('SchoolClass', on_delete=models.PROTECT, related_name='allocations')
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, related_name='allocations')
    hours = models.PositiveIntegerField()

    class Meta:
        unique_together = ('teacher', 'school_class', 'subject')
        indexes = [
            models.Index(fields=['school_class', 'subject']),
            models.Index(fields=['teacher']),
        ]
        ordering = ['school_class__nivel', 'school_class__clasa', 'subject__name']

    def clean(self):
        if self.teacher.nivel != self.school_class.nivel:
            raise ValidationError("Teacher level must match class level.")
        try:
            pr = PlanRow.objects.get(
                nivel=self.school_class.nivel,
                clasa=self.school_class.clasa,
                subject=self.subject
            )
            if self.hours > pr.ore:
                raise ValidationError(f"Hours exceed plan ({pr.ore}).")
        except PlanRow.DoesNotExist:
            pass

    def __str__(self):
        return f"{self.school_class}: {self.subject.name} – {self.teacher.name} ({self.hours}h)"


class ClassAssignment(models.Model):
    ROLE_CHOICES = [
        ('educator', 'Educator'),     # óvoda/alsó tagozat
        ('diriginte', 'Diriginte'),   # osztályfőnök
    ]
    school_class = models.OneToOneField('SchoolClass', on_delete=models.PROTECT, related_name='assignment')
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, related_name='class_assignments')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        ordering = ['school_class__nivel', 'school_class__clasa', 'school_class__litera']

    def clean(self):
        if self.teacher.nivel != self.school_class.nivel:
            raise ValidationError("Teacher level must match class level for class assignment.")

        if self.role == 'educator' and self.school_class.nivel not in ('anteprescolar', 'prescolar', 'primar'):
            raise ValidationError("Educator role is not typical for this level.")

    def __str__(self):
        return f"{self.school_class} — {self.role}: {self.teacher.name}"
