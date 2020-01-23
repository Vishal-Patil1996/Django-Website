from django.shortcuts import render
from .models import contact,Blog

# Create your views here.
def index(request):
    return render(request,'Blog/index.html')

def services(request):
    return render(request,'Blog/services.html')

def contacts(request):
    if request.method == 'POST':
        Your_name = request.POST.get('name')
        Your_email = request.POST.get('email')
        Subject= request.POST.get('subject')
        Your_Message= request.POST.get('messages')

        var_contact = contact(name=Your_name, email=Your_email, subject=Subject, messages=Your_Message)
        var_contact.save()
        return render(request,'Blog/index.html')

    else:
        return render(request,'Blog/contact.html')

def blog(request):
    var_1 = Blog.objects.all()  # whatever connected with object like date,time,title give to this var_1
    return render(request,'Blog/blog.html',{'var_1': var_1})

def single(request):
    return render(request,'Blog/blog-single.html')