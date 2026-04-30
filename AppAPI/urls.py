from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    # path('', views.home),
    # path('roles/', views.roles),
    path('APIRoles/', RolesListCreate.as_view(), name='APIRoles'),
    path('APIRoles/<int:pk>/', RolesUpdateDelete.as_view(), name='APIRoles'),
   
]
