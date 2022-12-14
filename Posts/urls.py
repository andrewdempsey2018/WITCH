from django.urls import path

from . import views

urlpatterns = [
    path('newpost/', views.newpost, name='newpost'),
    path('view_post/<slug>', views.view_post, name='view_post'),
    path('edit_post/<slug>', views.edit_post, name='edit_post'),
    path('delete_story/<int:id>', views.delete_story, name='delete_story'),
    path("newstory/", views.newstory, name="newstory"),
    path("stories/", views.stories, name="stories"),
    path('confirmed/', views.Confirmed.as_view(), name='confirmed'),
]