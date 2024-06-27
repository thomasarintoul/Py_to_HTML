from setuptools import setup, find_packages

setup(
    name="Py_to_HTML",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'ipython',
        'weasyprint',
        'matplotlib'
    ],
    author="Thomas A. Rintoul",
    author_email="RintoulTA@cardiff.ac.uk",
    description="A package for converting python objects to HTML code",
    url="https://github.com/thomasarintoul/Py_to_HTML",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
