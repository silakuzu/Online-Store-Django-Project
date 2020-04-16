from rest_framework import routers
from .api import categoriesViewSet

router = routers.DefaultRouter()
router.register('api/store',categoriesViewSet,'store')

urlpatterns = router.urls