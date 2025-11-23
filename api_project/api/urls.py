from django.urls import include, path
from .views import BookListCreateAPIView, BookViewSet, LoginView #The APIs are imported
#expanding functionality using DRF(routers)
from rest_framework.routers import DefaultRouter


#1. For the basic API (MANUAL URL MAPPING -function based routing) 
'''urlpatterns=[
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create')
]'''
#ka moja inawork ingine haiwork


#2. using the router one instead (AUTOMATIC URL GENERATION -view based routing)
'''router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = router.urls
'''

#3. combining both basic and full CRUD APIs
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns=[
    path('books/', BookListCreateAPIView.as_view(), name='book'),
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
      ]

