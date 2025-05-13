from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'animals', views.AnimalViewSet, basename='animal')
router.register(r'health', views.HealthRecordViewSet, basename='healthrecord')
router.register(r'productivity', views.ProductivityRecordViewSet, basename='productivityrecord')

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]