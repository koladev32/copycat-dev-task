from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .utils import parse_html


class HtmlParserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        html = request.data.get('html')

        html_data = parse_html(html)

        return Response({"data": html_data}, status=status.HTTP_200_OK)
