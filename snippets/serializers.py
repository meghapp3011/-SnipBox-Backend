from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Snippet, Tag

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class SnippetSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    tag_details = TagSerializer(source='tags', many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Snippet
        fields = [
            'id', 'title', 'note', 'created_by',
            'tags', 'tag_details', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        snippet = Snippet.objects.create(
            **validated_data)  # remove created_by here

        for tag_title in tags_data:
            tag, _ = Tag.objects.get_or_create(title=tag_title.strip().lower())
            snippet.tags.add(tag)

        return snippet

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data is not None:
            instance.tags.clear()
            for tag_title in tags_data:
                tag, _ = Tag.objects.get_or_create(
                    title=tag_title.strip().lower())
                instance.tags.add(tag)

        return instance
