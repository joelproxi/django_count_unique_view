from django.urls import path

from blog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/detail/', views.post_detail, name='detail'),
]