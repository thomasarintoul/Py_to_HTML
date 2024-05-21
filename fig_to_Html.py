"""
Author: T. A. Rintoul
Last Modified: 21/05/2024
Known Bugs:
- None

DESCRIPTION
An example script showing how to create a figure using Matplotlib and export it to an HTML file.
"""

import matplotlib.pyplot as plt

from functions_py_to_html import *

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot a straight line
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4]
ax.plot(x, y, label='Straight Line')

# Add labels and a legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Straight Line Plot')
ax.legend()

# Save the plot as an SVG file
fig.savefig('./outputs/plot.svg')

# Specify figure caption
fig_caption = r"""
A figure showing a straight line. Equation is $y = mx + c$
"""
fig_caption = preprocess_inline_maths(fig_caption)


# Export the figure to a .html file
html_report_head(output_filepath='./outputs/plot.html', font_family="Arial, sans-serif")


figure_to_html(figure_filepath='./outputs/plot.svg',
               fig_heading='Straight Line plot from Matplotlib',
               fig_caption=fig_caption,
               output_filepath='./outputs/plot.html',
               width=600,
               height=500)

html_report_foot(output_filepath='./outputs/plot.html')

