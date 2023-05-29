from django.contrib import admin
from .models import School, Programme, Department, Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ("school_name",)
    list_display = ("school_name",)
    search_fields = ("school_name__startswith",)
    ordering = ("school_name",)

    def __str__(self):
        return self.school_name
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ("department_name", "school")
    list_display = ("department_name", "school")
    list_filter = ("school",)
    search_fields = ("department_name__startswith",)
    ordering = ("department_name",)

    def __str__(self):
        return self.department_name
    
@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    fields = ("programme_name", "duration", "dept")
    list_display = ("programme_name", "duration", "dept")
    list_filter = ("dept",)
    search_fields = ("programme_name__startswith",)
    ordering = ("duration",)

    def __str__(self):
        return self.programme_name
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ("user", "programme", "roll_no", "batch",)
    list_display = ("user", "programme", "roll_no", "batch",)
    list_filter = ("programme","batch")
    search_fields = ("roll_no__startswith",)
    ordering = ("roll_no",)

    def __str__(self):
        return self.programme_name
