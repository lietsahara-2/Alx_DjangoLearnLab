from django.urls import path
from . import views
from .views import BookListAPIView, BookDetailAPIView, BookCreateAPIView, BookUpdateAPIView, BookDeleteAPIView

urlpatterns=[
    path("books/", BookListAPIView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailAPIView.as_view(), name="book-detail"),#<int:pk> for primary key of book instance
    path("books/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("books/update/<int:pk>/", BookUpdateAPIView.as_view(), name="book-update"),
    path("books/delete/<int:pk>/", BookDeleteAPIView.as_view(), name="book-delete")
]