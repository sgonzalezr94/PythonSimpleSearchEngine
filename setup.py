from setuptools import setup, find_packages

VERSION = "0.0.2"
DESCRIPTION = "PSSE"
LONG_DESCRIPTION = "A Python Simple Search Engine (PSSE) for documents using an inverted matrix and Okapi BM25."

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="psse",
    version=VERSION,
    author="Sebastian Gonzalez",
    author_email="sebastiang1493@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "psse", "search engine", "inverted matrix"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/sgonzalezr94/PythonSimpleSearchEngine",
)
