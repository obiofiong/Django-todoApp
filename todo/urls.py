from django.urls import path
from . import views

urlpatterns = [
    path('index', views.HomePageView,name = 'index'),
    path('add', views.addNewTodo,name = 'add'),
    path('commplete/<todo_id>', views.completeTodo,name = 'complete'),
    path('delete', views.deleteTodo,name = 'delete'),

]
