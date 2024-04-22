from django.shortcuts import render
from .models import SocialSection, Service ,Experience, Education, Profiles, Skill, Award, WorkDetail, Work, Post, Category, AboutSection

# Create your views here.
def home(request):
    about = AboutSection.objects.all()
    social = SocialSection.objects.all()[:2]
 
    data = {
        'about': about,
        'social': social
    }
    return render(request, 'index.html', data)

def about(request):
    about = AboutSection.objects.all()
    social = SocialSection.objects.all()[:2]
    education = Education.objects.all()
    experience = Experience.objects.all()
    data = {
        'about': about,
        'social': social,
        'education': education,
        'experience': experience,
    }
    return render(request, 'about.html', data)

def works(request):
    work = Work.objects.all()
    workdetail = WorkDetail.objects.all()
    data = {
        'work' : work,
        'workdetail' : workdetail,
    }
    return render(request, 'works.html', data)

def workdetails(request, url):
    workdetail = WorkDetail.objects.get(url = url)
    work = Work.objects.all()
    data = {
        'work' : work,
        'workdetail' : workdetail,
    }
    return render(request, 'work-details.html', data)

def service(request):
    social = SocialSection.objects.all()[:2]
    service = Service.objects.all()
    data = {
        'social': social,
        'service': service
    }
    return render(request, 'service.html', data)

def contact(request):
    about = AboutSection.objects.all()
    social = SocialSection.objects.all()
    data = {
        'about': about,
        'social': social
    }
    return render(request, 'contact.html', data)

def credentials(request):
    about = AboutSection.objects.all()
    social = SocialSection.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    award = Award.objects.all()
    skill = Skill.objects.all()
    data = {
        'about': about,
        'social': social,
        'education': education,
        'experience': experience,
        'award' : award,
        'skill' : skill,
    }
    return render(request, 'credentials.html', data)

def blog(request):
    category = Category.objects.all()
    post = Post.objects.all()
    data = {
        'category' : category,
        'post' : post,
    }
    return render(request, 'blog.html', data)

def blogdetails(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    data = {
        'category' : cats,
        'post' : post,
    }
    return render(request, 'blog-details.html', data)

def categorys(request, url):
    cats = Category.objects.get(url=url)
    post = Post.objects.all()
    data = {
        'category' : cats,
        'post' : post,
    }
    return render(request, 'category.html', data)
