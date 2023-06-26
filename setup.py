from setuptools import setup, find_packages

setup(
    name='foo-plugin',
    version='0.1',
    license='LICENSE',
    packages=find_packages(),
    description='Stuff that Ecosystem Tests Use',
    install_requires=['cloudify-common']
)
