from django.urls import path

from .views import (
    #manage
    manage_list,
    #page
    page_list,
    page_create,
    page_update,
    page_delete,
    #carousel
    carousel_create,
    carousel_list,
    carousel_update,
    carousel_delete
)


urlpatterns = [
    #manage:
    path('',manage_list,name='manage_list'),
    #carousel:
    path("carousel/list/",carousel_list,name="carousel_list"),
    path('carousel/create/', carousel_create, name='carousel_create'),
    path('carousel/update/<int:pk>/',carousel_update,name='carousel_update'),
    path('carousel/delete/<int:pk>/', carousel_delete, name='carousel_delete'),
    #page:
    path('page/list/',page_list,name='page_list'),
    path('page/create/', page_create, name='page_create'),
    path('page/update/<int:pk>/',page_update,name='page_update'),
    path('page/delete/<int:pk>/', page_delete, name='page_delete'),
    

    
    
] 