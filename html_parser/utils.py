import lxml.html

IGNORED_TAG_LIST = ['head', 'body', 'html']


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
        if el.tag in format_tag_count.keys():
            format_tag_count[el.tag]['count'] += 1
            format_tag_count[el.tag]['parent'] = el.getparent().tag if el.getparent() and el.getparent().tag not in \
                                                                       IGNORED_TAG_LIST else None
            format_tag_count[el.tag]['innerHTML'] = el.text
            format_tag_count[el.tag]['className'] = el.attrib.get('class')
            format_tag_count[el.tag]['value'] = el.attrib.get('value')
            format_tag_count[el.tag]['tag'] = el.tag

        else:
            format_tag_count[el.tag] = {
                'count': 1,
                'parent': el.getparent().tag if el.getparent() and el.getparent().tag not in IGNORED_TAG_LIST else None,
                'innerHTML': el.text,
                'className': el.attrib.get('class'),
                'value': el.attrib.get('value'),
                'tag': el.tag
            }
            if el.getparent():
                parents_nodes.add(el.getparent().tag)

    format_tag_count = {tag: value for (tag, value) in format_tag_count.items() if value['count'] >= 2}

    return [value for value in format_tag_count.values()]
