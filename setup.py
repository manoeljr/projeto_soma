from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="projeto_soma",
    version="0.0.1",
    author="Manoel Vieira",
    author_email="manoelv8@gmail.com",
    description="Projeto de teste empacotamento em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manoeljr/projeto_soma",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)
