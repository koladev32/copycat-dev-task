from bs4 import BeautifulSoup as BS
import lxml.html
from collections import Counter


def parse_html(html_data):
    """
    Get HTML and parse it.
    """

    format_html = lxml.html.fromstring(html_data)

    format_tag_count = {}

    # Creating a tag count and parent dict

    for el in format_html.iter():
        if el.tag in format_tag_count.keys():
            format_tag_count[el.tag]['count'] += 1
            format_tag_count[el.tag]['parent'] = el.getparent().tag
            format_tag_count[el.tag]['innerHTML'] = el.text
        else:
            format_tag_count[el.tag] = {
                'count': 1,
                'parent': el.getparent().tag if el.getparent() else None,
                'innerHTML': el.text
            }

    format_tag_count = {tag: value for (tag, value) in format_tag_count.items() if value['count'] >= 2}

    return format_tag_count
