from . import views 
from django.urls import path, include

urlpatterns = [
    path('',views.home, name="home"),
    path('book/',views.book_data, name="book")

]