from django.urls import path
from . import views

app_name='todos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('todos/', views.todos_view, name='todos'),
    path('todos/export', views.export_todos_to_excel, name='todos_export'),
]




































#    path('export/', views.export_todos_to_excel, name='todos:export'),






















































































# from django.urls import path
# from . import views

# app_name = 'todos'

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:todo_id>/delete', views.delete, name='delete'),
#     path('<int:todo_id>/update', views.update, name='update'),
#     path('add/', views.add, name='add'),
#     path('export/', views.export_todos_to_excel, name='export')
# ]










# from django.urls import path
# from . import views

# app_name='todos'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:todo_id>/delete', views.delete, name='delete'),
#     path('<int:todo_id>/update', views.update, name='update'),
#     path('add/', views.add, name='add'),
#     path('export/', views.export_todos_to_excel, name='todos:export')
# ]


























# from django.urls import path
# from . import views

# app_name = 'todos'

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:todo_id>/delete', views.delete, name='delete'),
#     path('<int:todo_id>/update', views.update, name='update'),
#     path('add/', views.add, name='add'),
#     path('export/', views.export_todos_to_excel, name='export')
# ]
