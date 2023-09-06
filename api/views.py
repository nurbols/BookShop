from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from books.models import Book 
from .serializers import BookSerializer 
# Create your views here.
class BookPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100 

class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id'] 
    search_fields = ['title', 'author']
    pagination_class = BookPagination

class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        try:
            prince = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'Price': 'Must be above $0.00' })
        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})
        return super().create(request, *args, **kwargs) 


class BookUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']), {
                'title':product['title'],
                'author':product['author'],
                'price':product['price'],
            })
        return response
        