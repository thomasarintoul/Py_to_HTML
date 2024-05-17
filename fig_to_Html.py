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
fig.savefig('plot.svg')

fig_caption = r"""
A figure showing a straight line. Equation is $y = mx + c$
"""
fig_caption = preprocess_inline_maths(fig_caption)

html_report_head(output_filepath='plot.html', font_family="Arial, sans-serif")


figure_to_html('plot.svg',
               output_filepath='plot.html')

html_report_foot(output_filepath='plot.html')

# html_template = f"""
#     <h1>Matplotlib Plot Embedded in HTML</h1>
#     <figure>
#         <object data="plot.svg" type="image/svg+xml" width="600" height="500"></object>
#         <figcaption>Figure Caption: {fig_caption}</figcaption>
#     </figure>
# </body>
# </html>
# """
#
# # Save the HTML to a file
# with open('plot.html', 'a') as f:
#     f.write(html_template)

