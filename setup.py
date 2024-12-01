from setuptools import setup, find_packages

setup(
    name="log-analyzer",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0.0",
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": [
            "log-analyzer=cli.commands:cli",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A modular log analysis tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)