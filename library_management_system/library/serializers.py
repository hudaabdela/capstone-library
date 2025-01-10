from rest_framework import serializers
from .models import Book, UserProfile, Borrow
from django.contrib.auth.models import User

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Serializer for the UserProfile model
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Serializer for the Borrow model
class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Show username instead of ID
    book = serializers.StringRelatedField()  # Show book title instead of ID

    class Meta:
        model = Borrow
        fields = '__all__'
