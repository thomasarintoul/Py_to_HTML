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
dict = {"Name": ['Anurag', 'Manjeet', 'Shubham',
                            'Saurabh', 'Ujjawal'],
                   "Address": ['Patna', 'Delhi', 'Coimbatore',
                               'Greater noida', 'Patna'],
                   "ID": [20123, 20124, 20145, 20146, 20147],
                   "Sell": [140000, 300000, 600000, 200000, 600000]}
df = pd.DataFrame(dict)

html_table = df.to_html(index=False)


styled_html_table = style_html_table(html_table, output_filepath='combined.html')

figure_to_html('plot.svg',
               output_filepath='combined.html')

output_text_to_html(markdown_content=markdown_content, output_filepath='combined.html')

html_report_foot(output_filepath='combined.html')

# Convert HTML to PDF
HTML('combined.html').write_pdf('combined.pdf')
