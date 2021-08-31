from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .utils import parse_html
from .parser import PlainTextParser
import json
from bs4 import BeautifulSoup


class HtmlParserView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (PlainTextParser,)

    def post(self, request, format=None):

        html_data = request.data.decode('UTF-8')
        html_data = json.loads(html_data)['html']

        response = parse_html(html_data)

        return Response({"data": response}, status=status.HTTP_200_OK)
