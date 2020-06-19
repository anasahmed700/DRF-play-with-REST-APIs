from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Profile, ProfileStatus
from .serializers import ProfileSerializer, ProfileStatusSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]