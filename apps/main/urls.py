from django.urls import path

from apps.main.views import author, create, details, explore, index

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('author/', author, name='author'),
    path('create/', create, name='create'),
    path('details/<int:pk>', details, name='details'),
    path('explore/', explore, name='explore'),
]
