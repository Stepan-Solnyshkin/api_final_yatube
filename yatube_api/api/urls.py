from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='api/v1/posts')
router.register('groups', GroupViewSet, basename='api/v1/groups')
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
    basename='api/v1/comments')
router.register('follow', FollowViewSet, basename='api/v1/follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
