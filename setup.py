import ast
from setuptools import setup, find_packages
from Cython.Build import cythonize


def get_version(file_name: str, version_name: str = "__version__") -> Optional[str]:
    with open(file_name) as f:
        tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if node.targets[0].id == version_name:
                    return node.value.s
    return "0.0.0"


class About(object):
    NAME = "MIPy-Talk"
    VERSION = get_version("pairwise_manhattan/__init__.py")
    AUTHOR = "blester125"
    EMAIL = f"{AUTHOR}@gmail.com"
    URL = f"https://github.com/{AUTHOR}/{NAME}"
    DL_URL = f"{URL}/archive/{VERSION}.tar.gz"
    LICENSE = "MIT"
    DESCRIPTION = "Code and Slides for Michigan Python Meetup talk"


setup(
    name=About.NAME,
    version=About.VERSION,
    description=About.DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author=About.AUTHOR,
    author_email=About.EMAIL,
    url=About.URL,
    download_url=About.DL_URL,
    license=About.LICENSE,
    python_requires=">=3.6",
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=["numpy",],
    extras_require={"test": ["pytest"],},
    keywords=["Numpy", "Optimization", "Numerical Computing"],
    entry_points={},
    ext_modules=cythonize("pairwise_manhattan/pairwise_manhattan_cython.pyx"),
    classifiers={
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    },
)
