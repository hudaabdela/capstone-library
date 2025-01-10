from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserProfileViewSet, BorrowViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'borrow', BorrowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
