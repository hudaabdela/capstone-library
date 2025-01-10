from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model to store books in the library
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    publication_date = models.DateField()
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

# User Profile to extend the built-in Django User model (optional)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(default=timezone.now)
    membership_type = models.CharField(max_length=100, choices=[('Regular', 'Regular'), ('Premium', 'Premium')], default='Regular')

    def __str__(self):
        return f"{self.user.username} Profile"

# Model to track borrowing of books
class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
    
    def is_overdue(self):
        if self.return_date is None and self.borrow_date:
            return timezone.now().date() > self.borrow_date + timezone.timedelta(days=14)  # 14 days loan period
        return False

# Create your models here.
