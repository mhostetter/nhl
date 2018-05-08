from setuptools import setup

setup(
    name="nhl",
    version="0.0.0",
    description="Python API for NHL game and player stats",
    long_description=open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",
    license="MIT",
    url="https://github.com/mhostetter/nhl",
    author="Matt Hostetter",
    author_email="matthostetter@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="nhl hockey sports stats api",
    packages=[
        "nhl",
    ],
    python_requires=">=3",
    project_urls={
        "Source": "https://github.com/mhostetter/nhl",
        "Tracker": "https://github.com/mhostetter/nhl/issues",
    },
)
