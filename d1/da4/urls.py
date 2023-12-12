from django.urls import path
from . import views

urlpatterns = [
   #path('',views.index, name='index'),
   #path('para/<int:nr>',views.index, name='para'),
   path('para/<str:key>/<int:name>/', views.index, name='Parameter 1 und 2'),
   ]