from django.urls import path
from .views import Home, More, Create, Edit, Delete

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/', More.as_view(), name='more'),
    path('create/', Create.as_view(), name='create'),
    path('post/<int:pk>/edit/', Edit.as_view(), name='edit'),
    path('post/<int:pk>/delete/', Delete.as_view(), name='delete')

]