from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/',views.sign_in, name='sign_in'),
    path('logout', views.logout_page, name='logout'),
    path('profile_register/', views.profile_register, name='profile_register'),
    path('profile_setting/', views.profile_setting, name='profile_setting'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('create_restoran/', views.create_restoran, name='create_restoran'),
    path('my_restoran_edit/', views.my_restoran_edit, name='my_restoran_edit'),
    path('my_restoran', views.my_restoran, name='my_restoran'),
    path('create_food/', views.create_food, name='create_food'),
    path('food_page/<int:id>/', views.food_page, name='food_page'),
    path('delete_food/<int:id>/', views.delete_food, name='delete_food'),
    path('edit_food/<int:pk>/', views.edit_food, name='edit_food'),
    path('restoran_page/<int:id>/', views.restoran_page, name='restoran_page'),
    path('food/<int:id>/', views.food, name='food'),
]