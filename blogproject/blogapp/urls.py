from django.urls import path
from blogapp import views


urlpatterns = [
    path('',views.home),
    path('about/', views.about),
    path('works/', views.works),
    path('works/<slug:url>', views.workdetails),
    path('service/', views.service),
    path('contact/', views.contact),
    path('credentials/', views.credentials),
    path('category/<slug:url>', views.categorys),
    path('blog/', views.blog),
    path('blog/<slug:url>', views.blogdetails),
]