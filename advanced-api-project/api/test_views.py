from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create an author and a book
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            author=self.author,
            publication_year=1997
        )

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])

    # CREATE
  
    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2020
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    
    # LIST / GET ALL
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    
    # RETRIEVE SINGLE BOOK
    
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")

 
    # UPDATE BOOK
  
    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "author": self.author.id,
            "publication_year": 2000
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    
    # DELETE BOOK
   
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

 
    # SEARCH FUNCTIONALITY
   
    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + "?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    # FILTER BY AUTHOR NAME
  
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author__name=Rowling")
        self.assertEqual(len(response.data), 1)

    # ORDERING
    
    def test_order_books_by_title(self):
        Book.objects.create(
            title="A Book",
            author=self.author,
            publication_year=2005
        )
        response = self.client.get(self.list_url + "?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "A Book")

   
    # PERMISSIONS TEST
   
    def test_unauthenticated_user_cannot_access(self):
        client = APIClient()  # not logged in
        response = client.get(self.list_url)
        self.assertIn(response.status_code, [401, 403])  # depending on your settings
