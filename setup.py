from setuptools import setup

setup(
	name = 'GitIssues',
	version = '1.0',
	py_modules = ['gi'],
	install_requires=[
		'Click',
		'requests'
	],
	entry_points=""" 
		[console_scripts]
		gi=gi:cli
	""",
)
