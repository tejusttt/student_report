from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import *

# Create your views here.

def get_student(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset= Student.objects.filter(
        Q(student_name__icontains=search) |
        Q(department__department__icontains=search) |
        Q(student_email__icontains=search) |
        Q(student_id__student_id__icontains=search)
            )
        
    
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'Student.html',{'queryset' : page_obj})


def see_marks(request, student_id):
    queryset = SubjectMark.objects.filter(student_id__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    
    
    max_marks = 600  
    
    total_marks_percentage = (total_marks['total_marks'] / max_marks) * 100 if total_marks['total_marks'] else 0
    
    return render(request, 'see_marks.html', {'queryset': queryset, 'total_marks': total_marks['total_marks'], 'total_marks_percentage': total_marks_percentage})
