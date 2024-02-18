from django.contrib import admin
from core.models import Department, Project, Shift, ShiftServices


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ShiftServices)
class ShiftServicesAdmin(admin.ModelAdmin):
    list_display = ['name']