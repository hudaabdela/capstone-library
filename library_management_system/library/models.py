from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(default=now)
    membership_type = models.CharField(max_length=100, choices=[('Regular', 'Regular'), ('Premium', 'Premium')], default='Regular')

    def __str__(self):
        return f"{self.user.username} Profile"

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=now)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def save(self, *args, **kwargs):
        if isinstance(self.borrow_date, datetime.datetime):
            self.borrow_date = self.borrow_date.date()
        if isinstance(self.return_date, datetime.datetime):
            self.return_date = self.return_date.date()
        super().save(*args, **kwargs)

# Create your models here.
