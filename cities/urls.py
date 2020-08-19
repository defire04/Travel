from django.urls import path
from .views import *
#from .views import home, CityDetailView, CityCreateView


urlpatterns = [
    path('', home, name='home'),
    #path('<int:pk>/', CityDetailView.as_view(), name='home'),
    path('add/', CityCreateView.as_view(), name='add'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),



    ] 
