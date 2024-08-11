from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirect root URL to login
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('home/', views.home, name='home'), 
    path('experience/', views.experience_view, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('education/', views.education, name='education'),# Add this for home page after login
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
   
]
