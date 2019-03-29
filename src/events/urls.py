from rest_framework import routers
from .viewsets import (
    EventListViewSet,
    ReporterListViewSet,
    EventTypeListViewSet,
)

router = routers.SimpleRouter()
router.register('events', EventListViewSet)
router.register('reporters', ReporterListViewSet)
router.register('types', EventTypeListViewSet)

urlpatterns = router.urls
