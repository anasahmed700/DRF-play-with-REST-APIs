from rest_framework import generics
from ..models import Quote
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly


# list & create concrete apiview class
class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# retrieve, update & destroy concrete apiview class
class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
