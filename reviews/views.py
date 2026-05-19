from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Book, Review
from .serializers import RegisterSerializer, BookSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsReviewOwner

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_id'])

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            book_id=self.kwargs['book_id']
        )

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsReviewOwner]

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            from rest_framework.response import Response
            return Response({"error": "Old password is incorrect"}, status=400)

        user.set_password(new_password)
        user.save()

        from rest_framework.response import Response
        return Response({"message": "Password changed successfully"})