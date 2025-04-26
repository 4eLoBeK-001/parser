from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_list),
    path('article/<int:article_id>/', views.article_detail, name='acrticle_detail'),
]
