from django.http import HttpResponse
from rest_framework.views import APIView

from cockroach.svg_creator import SvgCreator
from cockroach.serializers import BodySerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProjectionView(APIView):

    @swagger_auto_schema(
        operation_description="",
        operation_summary="Returns an svg file with a 2d projection.",
        request_body=BodySerializer,
        responses={200: openapi.Response('OK', openapi.Schema(type=openapi.TYPE_FILE,
                                                              format='image/svg+xml'))},
        operation_id='Projection'
    )
    def post(self, request):
        serializer = BodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        geometry = SvgCreator(serializer.data['geometry'], serializer.data['projection_plane'])
        return HttpResponse(geometry.generate_svg(), content_type='image/svg+xml')
