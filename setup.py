from setuptools import setup, find_packages

setup(
    name="pyDescribeNTSecurityDescriptor",
    version="1.0.0",
    author="KcanCurly",
    description="A python tool to parse and describe the contents of a raw ntSecurityDescriptor structure.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/pyDescribeNTSecurityDescriptor",
    packages=find_packages(),
    install_requires=[
        "ldap3",
        "sectools>=1.4.3",
        "pycryptodome"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "DescribeNTSecurityDescriptor=src.DescribeNTSecurityDescriptor:main",
        ],
    },
)