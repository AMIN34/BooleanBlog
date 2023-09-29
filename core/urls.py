from django.urls import path
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, categoryView, likeView



urlpatterns = [
    #path('', views.home, name="home") # This is used for function based view
    path("", HomeView.as_view(), name="home"), # This is used for class based view
    path('article/<int:pk>',ArticleView.as_view(),name="article"), # Dynamic URL
    path('add_post', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('article/add_Category', AddCategoryView.as_view(), name="add_category"),
    path('categories/<str:cats>', categoryView, name='category'),
    path('like/<int:pk>', likeView, name="post_like"),
]