from rest_framework import serializers


class GeometrySerializer(serializers.Serializer):
    x1 = serializers.IntegerField()
    x2 = serializers.IntegerField()
    y1 = serializers.IntegerField()
    y2 = serializers.IntegerField()
    z1 = serializers.IntegerField()
    z2 = serializers.IntegerField()


class BodySerializer(serializers.Serializer):
    geometry = GeometrySerializer(many=True)
    projection_plane = serializers.CharField(required=True, max_length=2)
