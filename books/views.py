from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	permission_classes = [IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
