from django.urls import path
from .views import JobOfferListCreateAPIView, JobOfferDetailAPIView

urlpatterns = [
    path('jobs/', JobOfferListCreateAPIView.as_view(), name='job-list'),
    path('jobs/<int:pk>', JobOfferDetailAPIView.as_view(), name='job-detail')

]