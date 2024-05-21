# Py_to_HTML: A simple package for creating HTML reports (with the option to export to PDF)

This is a simple package written to take in various data formats (strings, pandas dataframes and matplotlib figures as of 21/05/2024) and export them to HTML files that can be displayed in a browser or converted to a PDF format.

This function was written for producing reports in the sciences and as such supports LaTeX maths formatting using MathJax.
There is an optional function provided to allow conversion from the typical LaTeX formatting (i.e. `${maths here}$`) to that supported by MathJax (i.e. `\({maths here}\)`).

This package is designed to function with minimal requirements.
It is verified to work in Python 3.12.1 however should function in most versions of Python 3.

If you discover any bugs in this package, please do raise an issue.

For more complex issues, feel free to [email me](mailto:thomas@thomasrintoul.me).

## Instructions for Use
The required functions are found in `functions_py_to_html.py`.
- Every HTML file to be written to must first be created with a header using: `html_report_head`
- Every HTML file to be written to must be completed with a footer using: `html_report_foot`

Examples of how to use the functions can be found in:
- `example_md_to_html`: convert Markdown text to HTML
- `example_pandas_to_html`: convert a Pandas DataFrame to HTML Table
- `example_fig_to_html`: embed a MatPlotLib figure in an HTML document
