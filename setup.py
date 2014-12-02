try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'CSV Validation Tool',
	'author': 'Joshua Westgard',
	'url': 'http://github.com/jwestgard/csv-validate/',
	'download_url': 'Where to download it.',
	'author_email': 'westgard@umd.edu',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['validate'],
	'scripts': [],
	'name': 'csv-validate'
}

setup(**config)
