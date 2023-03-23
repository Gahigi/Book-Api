from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.ViewAllBooks.as_view()),
    path('book/<int:id>/', views.ViewBook.as_view()),
]
