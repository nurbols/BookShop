from django.urls import path 

from .views import BookAPIView, BookCreateView, BookUpdateDestroyView

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('new/', BookCreateView.as_view()), 
    path('<int:id>/', BookUpdateDestroyView.as_view()), 
]
