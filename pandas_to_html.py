import pandas as pd
from IPython.display import display, HTML

from functions_py_to_html import *

html_report_head(output_filepath='table_output.html', font_family="Arial, sans-serif")

# creating the dataframe
dict = {"Name": ['Anurag', 'Manjeet', 'Shubham',
                            'Saurabh', 'Ujjawal'],
                   "Address": ['Patna', 'Delhi', 'Coimbatore',
                               'Greater noida', 'Patna'],
                   "ID": [20123, 20124, 20145, 20146, 20147],
                   "Sell": [140000, 300000, 600000, 200000, 600000]}
df = pd.DataFrame(dict)

html_table = df.to_html(index=False)


style_html_table(html_table, output_filepath='table_output.html')



print("Styled HTML table has been saved to 'table_output.html'")

html_report_foot(output_filepath='table_output.html')