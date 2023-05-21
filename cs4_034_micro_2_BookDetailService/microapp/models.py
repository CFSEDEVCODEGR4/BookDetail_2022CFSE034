from django.db import models
from django.urls import reverse



# ===============================================================
# Book Model
# ===============================================================
class Book(models.Model):    
    book_id = models.CharField(max_length = 10) 
    book_name = models.CharField(max_length = 40)
    book_barcode = models.CharField(max_length = 120) 
    book_price = models.CharField(max_length = 20)
    book_quantity = models.CharField(max_length = 20)
    book_author = models.CharField(max_length = 20)
    class Meta:
        ordering = ['book_id']

    def get_absolute_url(self):
        return reverse('Book-details', args=[str(self.id)])   
        
    def __str__(self):
        return self.book_id
# ===============================================================






