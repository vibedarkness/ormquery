from django.shortcuts import render

from .models import *

# Create your views here.


def student_list(request):
    post=Student.objects.all()
    print(post.query)

    context={
        'post':post,
    }

    return render(request, 'output.html',context)