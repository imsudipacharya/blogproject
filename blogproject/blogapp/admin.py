from django.contrib import admin
from .models import SocialSection, Experience, Service, Education, Profiles, Skill, Award, WorkDetail, Work, Post, Category, AboutSection
# Register your models here.

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['content']

@admin.register(SocialSection)
class SocialSectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(WorkDetail)
class WorkDetailAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin): 
    list_display = ['title']