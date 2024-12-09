from django.urls import path
from blog import views

urlpatterns = [
    path('home/', views.PostViews.as_view(), name='home'), 
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
