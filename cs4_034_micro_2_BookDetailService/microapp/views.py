from django.shortcuts import render

from rest_framework import generics
from microapp.serializers import  BookSerializer
from microapp.serializers import  Book
               




# ===================================================
# Books
# ===================================================
class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        queryset = Book.objects.all()
        # Allow filter/search using mobile as query parameter
        in_book_id = self.request.query_params.get('book_id', None)
        if (in_book_id is not None):
            queryset = queryset.filter(user_id = in_book_id)
        return queryset

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
# ===============================================================
