import pathlib
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# This call to setup() does all the work
setuptools.setup(
   name='opensee',
   version='0.0.2',
   author='Mohsen Azimi',
   author_email='mohsen.azimi@ubc.ca',
   license='MIT',
   description="An Open-source Package for Structural & Earthquake Engineering",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url='https://github.com/mohsen-azimi/OpenSEE',
   packages=setuptools.find_packages(),
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
   include_package_data=True,
   install_requires=[],
   python_requires='>=3.8',
   entry_points={
        "console_scripts": [
            "opensee=testfunction.__main__:main",
        ]
    },

)
