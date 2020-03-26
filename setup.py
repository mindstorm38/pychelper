import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pychelper",
    version="0.1.5",
    author="Théo Rozier",
    author_email="contact@theorozier.fr",
    description="Python project compilation helper that compile python files and copy resource files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://theorozier.fr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
