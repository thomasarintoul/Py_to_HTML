"""
Author: T. A. Rintoul
Last Modified: 21/05/2024
Known Bugs:
- None

DESCRIPTION
An example script showing how define Markdown text, including LaTeX maths and covert to HTML file.
"""

import re

from functions_py_to_html import *

html_report_head(output_filepath='./outputs/output.html', font_family="Arial, sans-serif")

markdown_content = r"""
The galaxy mass is $5 \times 10^{13}$ M$_\odot$.
"""

output_text_to_html(markdown_content=markdown_content, output_filepath='./outputs/output.html')

html_report_foot(output_filepath='./outputs/output.html')