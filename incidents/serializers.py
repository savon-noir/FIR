from incidents.models import Incident
from rest_framework import serializers as rfserializers, viewsets


class IncidentAPISerializer(rfserializers.ModelSerializer):
    class Meta:
        model = Incident
