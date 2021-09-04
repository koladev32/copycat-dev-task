from bs4 import BeautifulSoup as BS
import lxml.html
from collections import Counter


def parse_html(html_data):
    """
    Get HTML and parse it.
    - Create a tag count and parent count
    - Filter tags with classname or value or id
    - Check if the parent is already present in the tag count and
    the parent count
    - Remove the tags with repeated parents
    """

    format_html = lxml.html.fromstring(html_data)

    format_tag_count = {}

    parents_nodes = set()

    # Creating a tag count and parent dict

    for el in format_html.iter():
        if el.tag in format_tag_count.keys() and el.attrib.get('class') == format_tag_count[el.tag].get('class') \
                and el.attrib.get('value') == format_tag_count[el.tag].get('value'):
            if el.getparent().tag:
                parents_nodes.add(el.getparent().tag)
            format_tag_count[el.tag]['count'] += 1
            format_tag_count[el.tag]['parent'] = el.getparent().tag
            format_tag_count[el.tag]['innerHTML'] = el.text
            format_tag_count[el.tag]['class'] = el.attrib.get('class')
            format_tag_count[el.tag]['value'] = el.attrib.get('value')

        else:
            if el.tag in format_tag_count.keys() and format_tag_count[el.tag].get('count') <= 2:
                continue
            format_tag_count[el.tag] = {
                'count': 1,
                'parent': el.getparent().tag if el.getparent() else None,
                'innerHTML': el.text,
                'class': el.attrib.get('class'),
                'value': el.attrib.get('value')
            }
            if el.getparent():
                parents_nodes.add(el.getparent().tag)

    format_tag_count = {tag: value for (tag, value) in format_tag_count.items() if value['count'] >= 2}

    for key in format_tag_count.copy():
        if key in parents_nodes:
            format_tag_count.pop(key)

    return format_tag_count
