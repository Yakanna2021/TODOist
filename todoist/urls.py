
from django.contrib import admin
from todoapp.views import addTodoView, deleteTodoView
from django.urls import include, path

urlpatterns = [
    path('todoapp/', include('todoapp.urls')),
    path('admin/', admin.site.urls),
    path('addTodoItem/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
]