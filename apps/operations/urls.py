from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeeListView.as_view(), name = 'home'),
    path('tree/<int:pk>/', views.tree, name = 'tree'),
    path('cousin/<int:pk>/', views.cousin, name = 'cousin'),
    path('sibling/<int:pk>/', views.sibling, name = 'sibling'),
]