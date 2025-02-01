from setuptools import setup, find_packages

setup(
    name="randerDataEngine",
    version="1.0.0",
    author="Your Name",
    description="A flexible template rendering engine using Jinja2.",
    packages=find_packages(),
    install_requires=["Jinja2"],
    include_package_data=True,
    package_data={"randerDataEngine": ["templates/**/*.j2"]},
)
