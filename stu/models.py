from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']
        
class StudentID(models.Model):
    student_id = models.CharField( max_length=100 )       
    
    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey( Department, related_name="depart", on_delete= models.CASCADE)
    student_id = models.OneToOneField( StudentID , related_name="studentid", on_delete= models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField(unique= True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()
    
    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class Subject(models.Model):
    department = models.ForeignKey(Department, related_name = "sub", on_delete = models.CASCADE)
    subject_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.subject_name} - {self.department}'
    
    class Meta:
        ordering=['department']
               
class SubjectMark(models.Model):
    student = models.ForeignKey(Student, related_name = "sub_marks", on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="sub_marks", on_delete = models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.student} - {self.subject} - Marks: {self.marks}"

    class Meta:
        unique_together= ['student','subject']
        
        
# class Reportcard(models.Model):8
#     student = models.ForeignKey(Student, related_name = "report_marks", on_delete = models.CASCADE)
#     st_rank = models.IntegerField()
#     date_of_report = models.DateField(auto_now_add = True)
    
#     class Meta:
#         unique_together =['date_of_report','st_rank']