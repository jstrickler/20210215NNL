from setuptools import setup
from setuptools import find_packages

setup(
    name='alpha',
    version='1.0',
    description='Amazing package',
    long_description='Really truly amazing....Long description here....',
    author='John Strickler',
    author_email='jstrickler@gmail.com',
    license='MIT',
    url='http://www.cja-tech.com/temperature',  # doesn't really exist
    # py_modules=['alpha'],
    packages=find_packages(exclude=['contrib', 'doc', 'tests']),
)
