from rest_framework import viewsets
from .models import Book, UserProfile, Borrow
from .serializers import BookSerializer, UserProfileSerializer, BorrowSerializer

# Viewset for Books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Viewset for UserProfiles
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Viewset for Borrow records
class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
