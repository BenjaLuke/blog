from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes  = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering =['-created_at'] # El menos lo hace de manera descentente. Al revés de lo normal
    filterset_fields =['post'] # Filtrar por post