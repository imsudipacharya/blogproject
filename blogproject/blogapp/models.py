from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



# Create your models here.
#Category Model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title
   
# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    ref = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default="Sudip", on_delete=models.SET_NULL, null=True, editable=False)
    creator_link = models.CharField(max_length=200, default='https://www.linkedin.com/in/imsudipacharya/')
    image1 = models.ImageField(upload_to='post/', null=True, blank=True)
    image2 = models.ImageField(upload_to='post/', null=True, blank=True)
    image3 = models.ImageField(upload_to='post/', null=True, blank=True)
    image4 = models.ImageField(upload_to='post/', null=True, blank=True)
    def __str__(self):
        return self.title
    
#Work Model
class Work(models.Model):
    w_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='work/', null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title
   
# Work Detail Mode
class WorkDetail(models.Model):
    wd_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Work, on_delete=models.CASCADE)
    ref = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default="Sudip", on_delete=models.SET_NULL, null=True, editable=False)
    creator_link = models.CharField(max_length=200, default='https://www.linkedin.com/in/imsudipacharya/')
    image1 = models.ImageField(upload_to='work_detail/', null=True, blank=True)
    image2 = models.ImageField(upload_to='work_detail/', null=True, blank=True)
    def __str__(self):
        return self.title
    
# Awards
class Award(models.Model):
    awd_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)

# Skill
class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

# Profiles
class Profiles(models.Model):
    prof_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

# Education
class Education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    startdate = models.CharField(max_length=200)
    enddate = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    collegename = models.CharField(max_length=200)
    collegelink = models.CharField(max_length=200)
    content = RichTextField()

# Experience
class Experience(models.Model):
    exp_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    startdate = models.CharField(max_length=200)
    enddate = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    companyname = models.CharField(max_length=200)
    companylink = models.CharField(max_length=200)
    content = RichTextField()


class AboutSection(models.Model):
    name = models.TextField()
    email1 = models.TextField('mail@acharyasudip.info.np', null=True, blank=True)
    email2 = models.TextField('mail@acharyasudip.info.np', null=True, blank=True)
    phone1 = models.TextField('9811111111', null=True, blank=True)
    phone2 = models.TextField('9811111111', null=True, blank=True)
    position = models.TextField()
    content = models.TextField()
    address = models.TextField('Kathmandu', null=True, blank=True)
    date = models.TextField(default='2080-03-30', null=True, blank=True)
    short_cont = models.TextField()
    movetext = RichTextField()
    image1 = models.ImageField(upload_to='about/', null=True, blank=True)
    image2 = models.ImageField(upload_to='about/', null=True, blank=True)
    image3 = models.ImageField(upload_to='about/', null=True, blank=True)
    sign = models.ImageField(upload_to='about/', null=True, blank=True)
    proj_thum = models.ImageField(upload_to='about/', null=True, blank=True)


    def save(self, *args, **kwargs):
        # Ensure only one instance of the AboutSection model exists
        if AboutSection.objects.exists() and not self.pk:
            raise Exception("You can only create one instance of the AboutSection.")
        super(AboutSection, self).save(*args, **kwargs)


class Service(models.Model):
    s_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    icon = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    creator_link = models.CharField(max_length=200, default='https://www.linkedin.com/in/imsudipacharya/')
    image = models.ImageField(upload_to='service/', null=True, blank=True)
    def __str__(self):
        return self.title
    

class SocialSection(models.Model):
    title = models.TextField()
    icon = models.TextField()
    link = models.TextField()
    def __str__(self):
        return self.title
    