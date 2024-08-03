"""
URL configuration for classmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from . import views
from . import crud

urlpatterns = [
    path("components/", include("components.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),

    # views
    path('', views.home_view, name='home'),
    path('seating/', views.seating_view, name='seating'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('lining_up/', views.lining_up_view, name='lining_up'),
    path('lists/', views.lists_view, name='lists'),
    path('settings/', views.settings_view, name='settings'),

    # crud 
    path('<str:student_name>/delete_student', crud.delete_student, name='delete_student'),
    path('add_student', crud.add_student, name='add_student'),

    # partials
    path('crud_dialog', views.crud_dialog),

]
