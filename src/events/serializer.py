import uuid
from .models import (
    Event,
    Reporter,
    EventType,
)
from datetime import datetime
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    uuid = serializers.CharField()
    reporter = serializers.CharField()
    type = serializers.CharField()

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        """Check that start is before finish."""
        uuid_data = uuid.UUID(validated_data.pop('uuid')).hex
        reporter_data = validated_data.pop('reporter')
        datetime_data = validated_data.pop('datetime')
        type_data = validated_data.pop('type')
        reporter_instance, created = Reporter.objects.get_or_create(
            name=reporter_data
        )
        type_instance, created = EventType.objects.get_or_create(
            name=type_data
        )
        event = Event.objects.create(
            **validated_data,
            uuid=uuid_data,
            reporter=reporter_instance,
            datetime=datetime.fromtimestamp(float('%s' % datetime_data)),
            type=type_instance,
        )
        return event


class ReporterSerializer(serializers.ModelSerializer):

    events = EventSerializer(many=True, read_only=True)
    number_events = serializers.IntegerField()

    class Meta:
        model = Reporter
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):

    events = EventSerializer(many=True, read_only=True)
    number_events = serializers.IntegerField()

    class Meta:
        model = EventType
        fields = '__all__'
