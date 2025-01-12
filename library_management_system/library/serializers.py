from rest_framework import serializers
from .models import Borrow, Book, UserProfile
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Borrow
        fields = ['id', 'book', 'borrow_date', 'return_date']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['borrow_date'] = instance.borrow_date.isoformat() if instance.borrow_date else None
        data['return_date'] = instance.return_date.isoformat() if instance.return_date else None
        data['book'] = {
            'id': instance.book.id,
            'title': instance.book.title
        }
        return data

    def validate(self, data):
        book = data.get('book')
        user = self.context['request'].user
        is_return_action = 'return_date' in data

        if not is_return_action:
            if book.available_copies <= 0:
                raise serializers.ValidationError({"book": "No copies of this book are currently available."})
            if Borrow.objects.filter(user=user, book=book, return_date__isnull=True).exists():
                raise serializers.ValidationError({"book": "You have already borrowed this book and not returned it."})

        return data

    def create(self, validated_data):
        book = validated_data['book']
        book.available_copies -= 1
        book.save()
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'return_date' in validated_data and instance.return_date is None:
            instance.book.available_copies += 1
            instance.book.save()
        return super().update(instance, validated_data)
