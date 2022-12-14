from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Posts.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('education/', views.education, name='education'),
    path('about/', views.education, name='about'),
]
