# Keyword argument list


def create_html(tag, text, **attribute):
    html = f'<{tag}'

    for key, value in attribute.items():
        html = f"{key} = '{value}'"

    html = html + f'>{text}</{tag}>'
    return html

html = create_html('p', 'Hello world', style='paragraf')
print(html)
html = create_html('a', 'Ini link')
print(html)