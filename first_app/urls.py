from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
     path('',views.index, name='index'),
      path('temp/',views.index1, name='index'),
      path('topicList/',views.topicList, name='topicList'),
      path('form',views.form_name_view, name='form_name'),
      path('users',views.users, name='users'),
      path('relative/',views.relative, name='relative'),
      path('inheritance/', views.inheritance, name="inheritance"),
      path('filter/', views.inheritanceFilter, name="filter"),
      path('register/', views.register, name="register"),
      path('user_login/', views.user_login,name="user_login"),
]
