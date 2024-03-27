from faker import Faker
from .models import *
import random
from django.db.models import Sum

fake = Faker()

n = int(input("Enter how many lines of fake data you want: "))

def seed_db(n):
    try:
        for _ in range(n):
            
            # Department
            department_objs = Department.objects.all()
            department = random.choice(department_objs)
            
            # Student ID
            student_id = f'STU-0{random.randint(100,999)}'
            student_id_obj = StudentID.objects.create(student_id=student_id)
            
            # Subjects for each department
            department_subjects = {
                'Biotechnical': [
                    "Molecular Biology",
                    "Genetic Engineering",
                    "Bioinformatics",
                    "Bioprocess Engineering",
                    "Immunology",
                    "Biochemistry"
                ],
                'Civil': [
                    "Structural Analysis",
                    "Geotechnical Engineering",
                    "Transportation Engineering",
                    "Environmental Engineering",
                    "Construction Management",
                    "Hydraulic Engineering"
                ],
                'Computer Science': [
                    "Data Structures and Algorithms",
                    "Database Management Systems",
                    "Operating Systems",
                    "Software Engineering",
                    "Artificial Intelligence",
                    "Computer Networks"
                ],
                'Electrical': [
                    "Circuit Analysis",
                    "Power Systems",
                    "Control Systems",
                    "Digital Signal Processing",
                    "Electronics",
                    "Electrical Machines"
                ],
                'Mechanical': [
                    "Thermodynamics",
                    "Fluid Mechanics",
                    "Heat Transfer",
                    "Solid Mechanics",
                    "Manufacturing Processes",
                    "Machine Design"
                ]
            }
            
            subjects = department_subjects.get(department.department, [])
                
            # Student
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 32)
            student_address = fake.address()
            
            student = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
            
            # Student Marks
            for subject_name in subjects:
                subject, created = Subject.objects.get_or_create(department=department, subject_name=subject_name)
                
                if subject.department != student.department:
                    continue
                
                # Check if SubjectMark already exists for this subject and student
                if not SubjectMark.objects.filter(student=student, subject=subject).exists():
                    marks = random.randint(20, 100)
                    
                    SubjectMark.objects.create(
                        student=student,
                        subject=subject,
                        marks=marks 
                    )
            
    except Exception as e:
        print(e)

seed_db(n)


# def gen_rank():
#     current_rank = -1
#     ranks = Student.objects.annotate(marks = Sum('SubjectMark_marks')).order_by('-marks','-student_age')
    
#     i = i
    
#     for rank in ranks:
#         Reportcard.objects.create(
#             student = rank,
#             st_rank = i
#         )
        
#     i = i + 1