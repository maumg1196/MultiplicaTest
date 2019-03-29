from rest_framework import viewsets
from .models import (
    Event,
    Reporter,
    EventType,
)
from .serializer import (
    EventSerializer,
    ReporterSerializer,
)


class ReporterListViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class EventTypeListViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = ReporterSerializer


class EventListViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(EventListViewSet, self).get_serializer(*args, **kwargs)
