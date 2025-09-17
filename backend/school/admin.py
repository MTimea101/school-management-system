from django.contrib import admin
from .models import Area, Subject, Teacher, SchoolClass, PlanRow

admin.site.register([Area, Subject, Teacher, SchoolClass, PlanRow])
