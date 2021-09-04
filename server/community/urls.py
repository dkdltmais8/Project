from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_get_post),
    path('<int:review_pk>/', views.review_detail),
    path('<int:review_pk>/update/', views.review_update),
    path('<int:review_pk>/delete/', views.review_delete),
    path('<int:review_pk>/comments/', views.comment_get_post),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comment_delete),
]
