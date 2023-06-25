from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in airplane_mode/__init__.py
from airplane_mode import __version__ as version

setup(
	name="airplane_mode",
	version=version,
<<<<<<< HEAD
	description="Hypothetical airline reservation system",
=======
	description="Hypothetical flight ticket system",
>>>>>>> f9d67fdf37192b1a07ac69c019709884cb0220c7
	author="Ton",
	author_email="ton@xurpas.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
