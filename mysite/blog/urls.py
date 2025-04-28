from django.urls import path
from blog.views import post_detail
from . import views

urlpatterns = [
    path('home/', views.PostViews.as_view(), name='home'), 
    path("<slug:slug>/", post_detail, name="post_detail"),
]
