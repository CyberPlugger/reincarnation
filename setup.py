from setuptools import setup, find_packages
import os

# Reading the long description from README.md
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Python package made for better PIP access"

setup(
    name="reincarnation",
    version="1.0.0",
    author="Andrew Sergeevich",
    author_email="jumpki11@hotmail.com",
    description="Python package made for better PIP access",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CyberPlugger/reincarnation",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.7',
    install_requires=[
        # List any external dependencies here if needed
    ],
)
