from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    # path('', include(home.urls)),
    path('', views.home, name = 'home'),
    path('donate/', views.donate, name = 'donate'),
    # path('hform', views.hform, name = 'hform'),
    path('donorhome', views.donorhome, name = 'donorhome'),
    path('register', views.register, name= 'register'),
    path('login', views.handlelogin, name = ''),
    # path('show', views.showthis, name = 'show'),
    path('home', views.hoshome),
    path('donorprofile/<int:donor_pk>', views.donorprofile, name = "donorprofile"),
    # path('/delete/<int:delete_no>', views.delete, name = 'delete'),
    path('feedback', views.feedback, name = "feedback"),
    path('submit_feedback', views.submit_feedback, name = "submit_feedback"),
    path('hosfeed/<int:donor_pk>', views.hosfeed, name="hosfeed"),
    path('bloodform/<int:donor_pk>', views.bloodform, name= "bloodform"),
    path('submit', views.submit, name = 'submit'),
    path('requests/<int:donor_pk>/<int:u_id>',views.requests, name = 'requests'),
    path('profile', views.profile, name = "profile"),
    path('logout/', views.handlelogout, name = 'logout'),
]
