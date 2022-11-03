from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('', views.Book.as_view(), name='book'),
    path('', views.About.as_view(), name='about'),
    path('', views.Menu.as_view(), name='menu'),
]
