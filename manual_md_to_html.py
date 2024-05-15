import re

def markdown_to_html(markdown_content, font_family="Arial, sans-serif"):
    # Convert headings
    markdown_content = re.sub(r'^# (.*)$', r'<h1>\1</h1>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^## (.*)$', r'<h2>\1</h2>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^### (.*)$', r'<h3>\1</h3>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^#### (.*)$', r'<h4>\1</h4>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^##### (.*)$', r'<h5>\1</h5>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^###### (.*)$', r'<h6>\1</h6>', markdown_content, flags=re.MULTILINE)

    # Convert bold and italic
    markdown_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_content)
    markdown_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown_content)

    # Convert bullet points with indentation
    markdown_content = re.sub(r'^(\s*)- (.*)$', r'\1<li>\2</li>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'(<li>(?:.*?</li>)+)', r'<ul>\1</ul>', markdown_content, flags=re.DOTALL)

    # Convert links
    markdown_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown_content)

    # Preserve line breaks
    markdown_content = markdown_content.replace('\n', '<br>')

    # Add font style
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            body {{
                font-family: {font_family};
            }}
        </style>
    </head>
    <body>
        {markdown_content}
    </body>
    </html>
    """
    return html_content

def preprocess_inline_math(markdown_content):
    # Replace single $ with \( ... \)
    markdown_content = re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$', r'\\(\1\\)', markdown_content)
    return markdown_content

def output_text_to_html(markdown_content, font_family="Arial, sans-serif", output_filepath='output.html'):

    markdown_content = preprocess_inline_math(markdown_content=markdown_content)

    html_content = markdown_to_html(markdown_content=markdown_content, font_family=font_family)

    with open(output_filepath, 'w') as f:
        f.write(html_content)


# Define the variable
value = 24.1234531

# Markdown content with formatted variable included
markdown_content = r"""
The galaxy mass is 10$^{13}$ M$_\odot$.
"""

# # Markdown content
# markdown_content = """
# # My Markdown Document
#
# This is a paragraph of text in **Markdown** format.
#
# - List item 1
# - List item 2
# - List item 3
#
# Here's a [link](https://example.com) to example.com.
#
# """

output_text_to_html(markdown_content=markdown_content)
