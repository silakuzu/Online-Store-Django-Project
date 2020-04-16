from store.models import categories
from rest_framework import viewsets, permissions
from .serializers import categoriesSerializer


class categoriesViewSet(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = categoriesSerializer