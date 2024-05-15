# importing pandas as pd
import pandas as pd
from IPython.display import display, HTML

# creating the dataframe
df = pd.DataFrame({"Name": ['Anurag', 'Manjeet', 'Shubham',
                            'Saurabh', 'Ujjawal'],
                   "Address": ['Patna', 'Delhi', 'Coimbatore',
                               'Greater noida', 'Patna'],
                   "ID": [20123, 20124, 20145, 20146, 20147],
                   "Sell": [140000, 300000, 600000, 200000, 600000]})






html_table = df.to_html(index=False)


def style_html_table(html_table):
    """
    Apply CSS styling to an HTML table.

    Args:
        html_table (str): HTML table string.

    Returns:
        str: Styled HTML table string.
    """
    styled_html_table = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
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
        {html_table}
    </body>
    </html>
    """
    return styled_html_table

styled_html_table = style_html_table(html_table)

# Write the styled HTML table to a file
with open('styled_table.html', 'w') as f:
    f.write(styled_html_table)

print("Styled HTML table has been saved to 'styled_table.html'")