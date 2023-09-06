from rest_framework import serializers
from books.models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id', 'title', 'author', 'photo', 'price', 'product_details'] 


    #def to_representation(self, instance):
        #data = super().to_representation(instance)
        #data['is_on_sale'] = instance.is_on_sale()
        #data['current_price'] = instance.is_on_price()
        #return data