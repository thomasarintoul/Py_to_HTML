import re
import pandas as pd

def markdown_to_html(markdown_content):
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
        {markdown_content}<br>
    """
    return html_content

def preprocess_inline_maths(markdown_content):
    # Replace single $ with \( ... \)
    markdown_content = re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$', r'\\(\1\\)', markdown_content)
    return markdown_content

def output_text_to_html(markdown_content, output_filepath='output.html'):

    markdown_content = preprocess_inline_maths(markdown_content=markdown_content)

    html_content = markdown_to_html(markdown_content=markdown_content)

    with open(output_filepath, 'a') as f:
        f.write(html_content)
        f.close()

def style_html_table(html_table, output_filepath='output.html'):
    """
    Apply CSS styling to an HTML table.

    Args:
        html_table (str): HTML table string.

    Returns:
        str: Styled HTML table string.
    """
    styled_html_table = f"""
        {html_table}<br>
    """

    # Write the styled HTML table to a file
    with open(output_filepath, 'a') as f:
        f.write(styled_html_table)
        f.close()

    return styled_html_table

def html_report_head(output_filepath='output.html', font_family="Arial, sans-serif"):
    html_header=f"""
    <!DOCTYPE html>
    <html>
    <head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            body {{
                font-family: {font_family};
            }}
            /* Define your CSS styles here */
            table {{
                font-family: Arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #dddddd;
                text-align: center;
                padding: 15px;
            }}
            th {{
                background-color: #c1d6f5;
            }}
            tr:nth-child(even) {{
                background-color: #c1d6f5;
            }}
        </style>
    </head>
    <body>
    """

    with open(output_filepath, 'w') as f:
        f.write(html_header)
        f.close()

def html_report_foot(output_filepath='output.html'):
    html_footer=f"""
    </body>
    </html>
    """

    with open(output_filepath, 'a') as f:
        f.write(html_footer)
        f.close()

def figure_to_html(figure_filepath, fig_heading='<br>', fig_caption='None', output_filepath='output.html',
                   width=600, height=500):
    fig_caption = preprocess_inline_maths(fig_caption)

    figure_html=f"""
    <h1>{fig_heading}</h1>
    <figure>
        <object data="{figure_filepath}" type="image/svg+xml" width="{width}" height="{height}"></object>
        <figcaption>Figure Caption: {fig_caption}</figcaption>
    </figure><br>
    """

    with open(output_filepath, 'a') as f:
        f.write(figure_html)
        f.close()