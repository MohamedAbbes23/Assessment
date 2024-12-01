from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, AssignmentViewSet, ChangePasswordView

router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet, basename='assignment')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]











