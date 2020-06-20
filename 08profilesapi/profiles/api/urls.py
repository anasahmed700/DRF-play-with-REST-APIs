from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ProfileList
from .views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView


# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

# routers configurations
router = DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("status", ProfileStatusViewSet)

urlpatterns = [
    # # path('profiles/', ProfileList.as_view(), name='profile-list'),
    # path('profiles/', profile_list, name='profile-list'),
    # path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
]
