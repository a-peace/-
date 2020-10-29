from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('table/<contract_id>/', views.table, name='table'),
    path('sсhedule', views.schedule, name='schedule'),
    path('uploads', views.uploads, name='uploads'),

    # Контракт ()
    path('create', views.create, name='create'),
    path('update_contract/<pk>/', views.update_contract, name='update_contract'),
    path('delete_contract/<pk>/', views.delete_contract, name='delete_contract'),

    # Сроки
    path('create_timing/<kek>/', views.create_timing, name='create_timing'),
    path('update_timing/<kek>/', views.update_timing, name='update_timing'),
    path('delete_timing/<kek>/', views.delete_timing, name='delete_timing'),


]
