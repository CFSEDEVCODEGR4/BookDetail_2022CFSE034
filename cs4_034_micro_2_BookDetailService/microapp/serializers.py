from rest_framework import serializers
from microapp.models import Book


# ============================================================
# Books
# ============================================================
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
                  'id',
                  'book_id', 
                  'book_name',
                  'book_barcode',
                  'book_price',
                  'book_quantity', 
                  'book_author',
                ]        
# ============================================================
