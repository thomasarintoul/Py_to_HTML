"""
Author: T. A. Rintoul
Last Modified: 21/05/2024
Known Bugs:
- markdown_to_html: cannot handle nested bullet pointed lists
"""

import re
import pandas as pd

def markdown_to_html(markdown_content):
    """
    Convert Markdown text to HTML code converting heading, bold/italic, bullet point and link notation
    into HTML format

    INPUTS:
        - markdown_content
            - type: str
            - desc: a string containing text formatted as in Markdown
    OUTPUTS:
        - html_content
            - type: str
            - desc: a string containing HTML formatted text
    """
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
    """
    Preprocess Markdown text for inline maths formatted in standard Latex style of ${maths here}$
    to the MathJax format of \({maths here}\).

    INPUTS:
        - markdown_content
            - type: str
            - desc: a string containing text formatted as in Markdown
    OUTPUTS:
        - markdown_content
            - type: str
            - desc: a string containint Markdown text with maths formatting
                    converted from ${maths here}$ to \({maths here}\).
    """
    markdown_content = re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$', r'\\(\1\\)', markdown_content)

    return markdown_content

def output_text_to_html(markdown_content, output_filepath='output.html'):
    """
    Function takes in Markdown (.md) text and converts it to html text.
    INPUTS:
        - markdown_content
            - type: str
            - desc: a string containing text formatted as in Markdown
        - output_filepath
            - type: str
            - desc: Relative or Absolute path of the output html file
    OUTPUTS:
        - appends formatted html text to output_filepath
    """

    markdown_content = preprocess_inline_maths(markdown_content=markdown_content)

    html_content = markdown_to_html(markdown_content=markdown_content)

    with open(output_filepath, 'a') as f:
        f.write(html_content)
        f.close()

def style_html_table(html_table, output_filepath='output.html'):
    """
    Function formats table for output file and appends to that file.

    INPUTS:
        - html_table
            - type: str
            - desc: HTML table

    OUTPUTS:
        - Writes to file

    """
    styled_html_table = f"""
        {html_table}<br>
    """

    # Write the styled HTML table to a file
    with open(output_filepath, 'a') as f:
        f.write(styled_html_table)
        f.close()


def html_report_head(output_filepath='output.html', font_family="Arial, sans-serif"):
    """
    Creates document at filepath specified and writes code head supporting MathJax LaTeX,
    defining font families and styling tables.

    INPUTS:
        - output_filepath:
            - type: str
            - desc: A relative or absolute filepath for the output file
        - font_family:
            - type: str
            - desc: String specifying the font family to use in this HTML file.
    OUTPUTS:
        - Writes HTML header to file specified by output_filepath
    """

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
    """
    Appends end to document at filepath specified.

    INPUTS:
        - output_filepath:
            - type: str
            - desc: A relative or absolute filepath for the output file
    OUTPUTS:
        - Writes HTML footer to file specified by output_filepath
    """
    html_footer=f"""
    </body>
    </html>
    """

    with open(output_filepath, 'a') as f:
        f.write(html_footer)
        f.close()

def figure_to_html(figure_filepath, fig_heading='<br>', fig_caption='None', output_filepath='output.html',
                   width=600, height=500):
    """
    Embeds figure in HTML file specified.

    INPUTS:
        - figure_filepath:
            - type: str
            - desc: A relative or absolute filepath for the figure to be embedded
        - fig_heading
            - type: str
            - desc: Text of heading to be displayed above figure
        - fig_caption:
            - type: str
            - desc: Text of caption to be displayed below figure
        - output_filepath:
            - type: str
            - desc: A relative or absolute filepath for the output file
        - width:
            - type: int
            - desc: Width of the figure in pixels
        - height:
            - type: int
            - desc: Height of the figure in pixels
    OUTPUTS:
        - Writes HTML figure to file specified by output_filepath
    """
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