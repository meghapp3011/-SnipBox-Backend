from .views import SnippetViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'snippets', SnippetViewSet, basename='snippet')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = router.urls

