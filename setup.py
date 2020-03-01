import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataStructure", # Replace with your own username
    version="0.0.1",
    author="Reinaldo Junio Dias de Abreu",
    author_email="reinaldodiasabreu@gmail.com",
    description="Package with several data structures implemented.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="", # Github repository
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)