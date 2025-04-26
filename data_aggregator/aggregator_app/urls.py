from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_list),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/<int:article_id>/upvote/', views.article_upvote, name='article_upvote'),
    path('article/<int:article_id>/downvote/', views.article_downvote, name='article_downvote'),

]
