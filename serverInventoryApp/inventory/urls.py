from django.urls import path
from . import views


urlpatterns = [

    path('', views.inventory , name='inventory' ),
    path('serverInfo/<str:pk>/',views.serverInfo, name='serverInfo'),


    #Path for Creating forms
    path('new-asset/', views.createAsset, name = 'new-asset'),
    path('new-location/,', views.createLocation, name = 'new-location'),

    #Path for Updating Forms
    path('update-asset/<str:pk>/', views.updateAsset, name ='update-asset'),
    path('delete-asset/<str:pk>/', views.deleteAsset, name = 'delete-asset'),

    #location page
    path('locationspage/', views.location, name='location'),
]