from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.

# 
admin.site.register(StudentID),
admin.site.register(Student),
admin.site.register(Department),
admin.site.register(Subject),
admin.site.register(SubjectMark),

# class ReportcardAdmin(admin.ModelAdmin):
#     list_display = ['student', 'st_rank','total_marks','date_of_report']
#     ordering = ['st_rank']
    
#     def total_marks(self,obj):
#         sub_marks = SubjectMark.objects.filter(student =obj.student)
#         marks = (sub_marks.aaggregate(marks = Sum('marks')))
#         return marks['marks']

# admin.site.register(Reportcard, ReportcardAdmin ),

