import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maidwhite",
    version="0.0.1",
    author="Pichu Chen",
    author_email="pichu@tih.tw",
    description="Maid White SDK in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tihtw/maidwhite-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
