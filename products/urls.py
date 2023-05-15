from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:product_id>/', views.detail),
    path('form/', views.form_view),
    path('update/<int:product_id>/', views.update),
    path('contact/', views.contact),
]