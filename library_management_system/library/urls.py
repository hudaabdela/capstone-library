from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserProfileViewSet, BorrowViewSet, UserViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'borrow', BorrowViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]