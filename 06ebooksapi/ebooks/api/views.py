from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.validators import ValidationError
from rest_framework.generics import get_object_or_404

from .permissions import IsAdminOrReadOnly, IsReviewAuthorOrReadOnly
from ..models import Ebook, Review
from .serializers import EbookSerializer, ReviewSerializer
from .pagination import SmallSetPagination


# Concrete API View Class
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("id")
    serializer_class = EbookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = SmallSetPagination  # added pagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        # serializer.save(ebook=ebook)
        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this book!")
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

# # Generic API View Class
# class EbookListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
