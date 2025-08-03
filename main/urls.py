"""
URL configuration for taskmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#this is the main url router for this project
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from todolist_app import views as todolist_views

#http = a language to communicate between client and server
# def home(request):
#     return HttpResponse("Welcome to TaskMate Homepage!")  # Simple response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name ='index'),
    path('todolist/',include('todolist_app.urls')),
    path('contact/',todolist_views.contact,name = 'contact'),
    path('about/',todolist_views.about,name = 'about'),
    path('account/',include('users_app.urls'),name = 'account'),          
    #the name tag is for referencing in other scripts like templates      
    # # after finding https://..../todolist/ it will redirect to todolist_app.url
]

#when we see the server we are visiting an empty server when we do "https..../admin" we are
#hitting then admin.site.urls function
