from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_table, name='plant_table'),
    path('plant/<int:pk>/detail/', views.get_plant, name="plant_detail"),
    path('plant/new/detail/<int:pk>', views.new_plant, name="plant_new_detail"),
    path('plant/add/', views.add_plant, name="add_plant"),
    path('record/add/', views.add_record, name="add_plant_record"),
    path('record/<int:pk>/edit/', views.plant_record, name="edit_plant_record"),
]
