from django.urls import path
from html_parser.views import HtmlParserView


urlpatterns = [
    path('parse_html/', HtmlParserView.as_view(), name='html-parser')
]