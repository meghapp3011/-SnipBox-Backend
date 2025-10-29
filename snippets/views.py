from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], url_path='overview')
    def overview(self, request):
        snippets = self.get_queryset()
        total_count = snippets.count()
        serializer = self.get_serializer(snippets, many=True)
        return Response({
            "total_snippets": total_count,
            "snippets": serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        remaining = self.get_queryset()
        serializer = self.get_serializer(remaining, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='snippets')
    def tag_snippets(self, request, pk=None):
        tag = self.get_object()
        snippets = tag.snippets.filter(created_by=request.user)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
