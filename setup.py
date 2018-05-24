
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jmeterWebReport",
    version="0.0.4",
    author="mark",
    author_email="mamian521@gmail.com",
    license="Apache License",
    description="More convenient to show JMeter's web page report",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magaofei/jmeterWebReport",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)