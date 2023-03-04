from distutils.core import setup
import py2exe

setup(
    name="SearchEach",
    version="1.0.0",
    description="Search everything inside two characters",
    author="ESFLOWNK",
    author_email="otakuflownk@gmail.com",
    scripts=["searcheach.py"],
    console=["searcheach.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None
)
