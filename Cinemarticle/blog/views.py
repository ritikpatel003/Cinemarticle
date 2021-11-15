from django.shortcuts import render
from .models import Blog
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    sno = [i for i in range(len(blogs))]
    return render(request, 'blog/index.html',{'blogs':blogs, 'sno':sno})

def content(request):
    name = request.GET.get('name','')
    blogs = Blog.objects.all()
    for i in blogs:
        if i.blog_name == name:
            blog = i.content
            image = i.image
            trailer = i.trailer
    trailer = trailer[0:7]+' class="hero" '+trailer[8:]
    return render(request, 'blog/content.html', {'name':name, 'blog':blog, 'image':image, 'trailer':trailer})

def contact(request):
    return render(request, 'blog/contact.html')

def mail(request):
    name = request.POST.get('name','')
    email = request.POST.get('email', '')
    phno = request.POST.get('phno', 'Not Provided')
    text = request.POST.get('text', '')
    send_mail(
        'Cinemarticle Mail from '+name,
        text+'\nemail: '+email+'\nphone no.: '+phno,
        settings.EMAIL_HOST_USER,
        ['ritikpatel003@gmail.com']
    )
    send_mail(
        'Your Message has been received',
        'Here is the details to review\nName: '+name+'\nEmail: '+email+'\nPhone No.: '+phno+'\nMessage: '+text,
        settings.EMAIL_HOST_USER,
        [email]
    )
    return render(request, 'blog/mail.html', {'name':name})