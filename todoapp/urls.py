from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('addTodoitems/',views.addTodoView),
    path('deleteTodoItem/<int:i>/',views.deleteTodoView)
]