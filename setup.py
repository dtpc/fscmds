from setuptools import find_packages, setup

tests_require = [
    "black>=20.8b1",
    "flake8>=3.8.0",
    "flake8-isort>=4.0.0",
    "isort>=5.1.0",
]


setup(
    name="fstree",
    author="dtpc",
    license="MIT License",
    description="CLI tool to print a filesystem tree",
    python_requires=">=3.8.0",
    packages=find_packages(exclude=("tests")),
    setup_requires=["setuptools_scm"],
    install_requires=[
        "click>=5.0",
        "fsspec",
        "treelib",
    ],
    extras_require={"test": tests_require},
    tests_require=tests_require,
    entry_points={
        "console_scripts": [
            "fstree = fstree.cli:main",
        ],
    },
)
