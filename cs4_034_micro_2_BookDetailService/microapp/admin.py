from django.contrib import admin

from .models import Book

# =======================================================
# Controls the fields to display in admin panel
# =======================================================

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'id',
                  'book_id', 
                  'book_name',
                  'book_barcode',
                  'book_price',
                  'book_quantity', 
                  'book_author',
                    )
admin.site.register(Book, BookAdmin)

# ===============================================================
