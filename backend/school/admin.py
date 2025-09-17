from django.contrib import admin
from .models import Area, Subject, Teacher, SchoolClass, PlanRow
from .models import Allocation, ClassAssignment


admin.site.register([Area, Subject, Teacher, SchoolClass, PlanRow])
@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'subject', 'teacher', 'hours')
    list_filter = ('school_class__nivel', 'subject__area')
    search_fields = ('teacher__name', 'subject__name', 'school_class__name')

@admin.register(ClassAssignment)
class ClassAssignmentAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'role', 'teacher')
    list_filter = ('school_class__nivel', 'role')
    search_fields = ('teacher__name', 'school_class__name')