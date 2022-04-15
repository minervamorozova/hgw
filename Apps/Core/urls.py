from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerUser/', views.registerUser),
    path('editionUser/<idUser>', views.editionUser),
    path('editUser/', views.editUser),
    path('deleteUser/<idUser>', views.deleteUser),
]