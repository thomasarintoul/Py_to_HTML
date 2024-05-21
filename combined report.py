"""
Author: T. A. Rintoul
Last Modified: 21/05/2024
Known Bugs:
- None

DESCRIPTION
An example script showing how to create a basic HTML report including Markdown text,
a Pandas Dataframe (converted to HTML table), and a Matplotlib plot (embedded in HTML).
"""

import re
import pandas as pd
from IPython.display import display, HTML
from weasyprint import HTML

from functions_py_to_html import *

html_report_head(output_filepath='combined.html', font_family="Arial, sans-serif")

markdown_content = r"""
The galaxy mass is $5 \times 10^{13}$ M$_\odot$.
"""

output_text_to_html(markdown_content=markdown_content, output_filepath='combined.html')

# creating the dataframe
dict = {"Name": ['Amy', 'Mike', 'Shona', 'Sam', 'Victor'],
        "Address": ['England', 'Wales', 'Scotland', 'Northern Ireland', 'Isle of Man'],
        "ID": [15640, 51562, 21561, 48106, 40854],
        "Score": [50, 90, 54, 75, 84]}
df = pd.DataFrame(dict)

html_table = df.to_html(index=False)


style_html_table(html_table, output_filepath='combined.html')

figure_to_html('plot.svg',
               output_filepath='combined.html')

output_text_to_html(markdown_content=markdown_content, output_filepath='combined.html')

html_report_foot(output_filepath='combined.html')

# Convert HTML to PDF
HTML('combined.html').write_pdf('combined.pdf')
