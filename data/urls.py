from django.urls import path
from . import views 


urlpatterns = [ 
   
    path('index/',views.index, name = "index"),
    path('about/',views.about, name = "about"),
    path('',views.welcome, name = "welcome"),
    path('create_unit/',views.createUnit, name = "create_unit"),
    path('delete_unit/',views.deleteUnit, name = "delete_unit"),
    path('update_unit/',views.updateUnit, name = "update_unit"),

         
]