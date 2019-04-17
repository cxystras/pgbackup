from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='Chris Xystras',
    author_email='cxystras@gmail.com',
    description='A utility for backing up PostgreSQL databases - case study',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cxystras/pgbackup',
    packages=find_packages('src')
)
