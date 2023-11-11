from django.urls import path
from . import views


urlpatterns = [
    path('', views.marvelcomics_home, name="marvelcomics_home"),
    path('create/', views.marvelcomics_create, name="marvelcomics_create"),
    path('shelf/', views.marvelcomics_shelf, name="marvelcomics_shelf"),
    path('<int:pk>/details/', views.marvelcomics_details, name="marvelcomics_details"),
    path('<int:pk>/update/', views.marvelcomics_update, name="marvelcomics_update"),
    path('<int:pk>/delete/', views.marvelcomics_delete, name="marvelcomics_delete"),
    path('bs/', views.marvelcomics_bs, name="marvelcomics_bs"),
    path('api/', views.marvelcomics_api, name="marvelcomics_api"),
]
