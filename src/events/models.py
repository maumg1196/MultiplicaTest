from django.db import models
from geoposition.fields import GeopositionField
from unixtimestampfield.fields import UnixTimeStampField


class Reporter(models.Model):
    """Reporter's Fields."""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Reporter"
        verbose_name_plural = "Reporters"

    def __str__(self):
        return self.name

    @property
    def number_events(self):
        return self.events.count()


class EventType(models.Model):
    """Event Type's Fields."""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Event Type"
        verbose_name_plural = "Events Types"

    def __str__(self):
        return self.name

    @property
    def number_events(self):
        return self.events.count()


class Event(models.Model):
    """Event's Fields."""

    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
    )
    name = models.CharField(max_length=50)
    reporter = models.ForeignKey(
        'Reporter',
        related_name='events',
        on_delete=models.PROTECT,
    )
    description = models.TextField()
    type = models.ForeignKey(
        'EventType',
        related_name='events',
        on_delete=models.PROTECT,
    )
    location = GeopositionField()
    datetime = UnixTimeStampField(use_numeric=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name
