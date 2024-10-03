from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "PSSE"
LONG_DESCRIPTION = (
    "A Python Simple Search Engine (PSSE) for documents using an inverted matrix."
)

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
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Linux :: Ubuntu",
        "Operating System :: Microsoft :: Windows",
    ],
)
