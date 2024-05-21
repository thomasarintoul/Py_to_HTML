"""
Author: T. A. Rintoul
Last Modified: 21/05/2024
Known Bugs:
- None

DESCRIPTION
An example script showing how to create pandas dataframe and export it to an HTML file as an HTML table.
"""

import pandas as pd
from IPython.display import display, HTML

from functions_py_to_html import *

html_report_head(output_filepath='table_output.html', font_family="Arial, sans-serif")

# creating the dataframe
dict = {"Name": ['Amy', 'Mike', 'Shona', 'Sam', 'Victor'],
        "Address": ['England', 'Wales', 'Scotland', 'Northern Ireland', 'Isle of Man'],
        "ID": [15640, 51562, 21561, 48106, 40854],
        "Score": [50, 90, 54, 75, 84]}
df = pd.DataFrame(dict)

html_table = df.to_html(index=False)


style_html_table(html_table, output_filepath='table_output.html')



print("Styled HTML table has been saved to 'table_output.html'")

html_report_foot(output_filepath='table_output.html')