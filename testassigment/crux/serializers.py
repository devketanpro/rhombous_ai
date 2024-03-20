from rest_framework import serializers
from .models import Record, Column


class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = "__all__"


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = "__all__"
