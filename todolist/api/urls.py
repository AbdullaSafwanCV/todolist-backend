from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddNoteViewSet

router = DefaultRouter()
router.register(r'todos', AddNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
