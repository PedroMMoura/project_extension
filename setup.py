from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_extension/__init__.py
from project_extension import __version__ as version

setup(
	name="project_extension",
	version=version,
	description="Project extension to connect to the developed Tasklist app and to provide extra integration functionalities.",
	author="Diogo Livio",
	author_email="d.livio@campus.fct.unl.pt",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
