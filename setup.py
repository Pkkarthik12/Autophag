from setuptools import setup, find_packages

setup(
    name="autophagx",
    version="0.1.0",
    packages=find_packages(),
    author="Autophag-X Team",
    description="A framework for Autophagic (Self-Consuming) Robotics AI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/autophagx/autophagx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Robotics",
    ],
    python_requires='>=3.8',
)
