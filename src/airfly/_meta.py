# NOTE: This file is auto-generated by "inv sync-meta"


name = "airfly"
version = "1.0.0"
description = "Auto generate Airflow's dag.py on the fly"
authors = [{"name": "ryanchao2012", "email": "ryanchao2012@gmail.com"}]
readme = "README.md"
license = {"text": "MIT"}
classifiers = [
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
dependencies = [
    "attrs",
    "cattrs",
    "regex",
    "networkx",
    "black",
    "isort",
    "click",
    "libcst",
    "asttrs",
]
scripts = {"airfly": "airfly.cli.main:main"}
