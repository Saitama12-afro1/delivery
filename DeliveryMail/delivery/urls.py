from django.urls import path
from . import views
app_name = "delivery"
urlpatterns = [
    path('', views.index, name = "index"),
    path('create_client/', views.create_client, name = "create_client"),
    path('check_clients/', views.check_clients, name = "check_client"),
    path('check_clients/update_client/<int:id>/', views.update_client, name = "update_client"),
    path('check_clients/delete_client/<int:id>/', views.delete_client, name = "delete_client"),
    path('create_delivery/', views.create_delivery, name = "create_delivery"),
    path('update_delivery/<int:id>/', views.update_delivery, name = "update_delivery"),
    path('delete_delivery/<int:id>/', views.delete_delivery, name = "delete_delivery"),
]