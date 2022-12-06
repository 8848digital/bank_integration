from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bank_integration/__init__.py
from bank_integration import __version__ as version

setup(
	name="bank_integration",
	version=version,
	description="Banking Integration for ErpNext",
	author="8848 Digital LLP",
	author_email="contact@8848digital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
